import math

MOD = int(1e16)

def count(n):
    """Returns the count of numbers of at most n digits where one digit is the sum of all other digits."""
    parts = [[]]
    for d in range(1, 10):
        ways = [(d,)]

        for k in range(1, d):
            for way in parts[d - k]:
                if way[-1] <= k:
                    ways.append(way + (k,))

        parts.append(ways)

    choose = [[1]]
    for i in range(n + 1):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[-1] + choose[-1][j - 1])

        choose.append(row)

    ans = 0
    for i in range(2, n + 1):
        for d in range(1, 10):
            for way in parts[d]:
                if len(way) + 1 > i:
                    continue

                freq = [0 for _ in range(10)]
                for x in way:
                    freq[x] += 1
                freq[d] += 1
                order = math.factorial(len(way) + 1)
                for x in freq:
                    order //= math.factorial(x)

                ans += order * choose[i - 1][i - len(way) - 1] % MOD
                ans %= MOD

    return ans


def S(n):
    # dp[len][mask of digs][dig sum] = (sum of opts, count of opts)
    MAX_SUM = 19
    dp = [[[0, 0] for _ in range(MAX_SUM)] for _ in range(1 << 9)]
    for d in range(1, 10):
        dp[1 << (d - 1)][d] = (d, 1)

    del d

    ans = 0
    for k in range(2, n + 1):
        ndp = [[[0, 0] for _ in range(MAX_SUM)] for _ in range(1 << 9)]
        for mask in range(1 << 9):
            for s in range(MAX_SUM):
                if dp[mask][s][1] == 0:
                    continue

                for nd in range(10):
                    if s + nd >= MAX_SUM:
                        break

                    new_mask = mask | (1 << (nd - 1)) if nd > 0 else mask
                    ndp[new_mask][s + nd][0] += 10 * dp[mask][s][0] + nd * dp[mask][s][1]
                    ndp[new_mask][s + nd][0] %= MOD
                    ndp[new_mask][s + nd][1] += dp[mask][s][1]
                    ndp[new_mask][s + nd][1] %= MOD

        dp = ndp

        for mask in range(1 << 9):
            for d in range(1, 10):
                if mask & (1 << (d - 1)):
                    ans += dp[mask][d + d][0]
                    ans %= MOD


    return ans


def main():
    print("S(3)", S(3))
    print("S(7)", S(7))
    print("S(2020)", S(2020))
    

if __name__ == "__main__":
    main()
