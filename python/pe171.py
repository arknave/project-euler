from fractions import Fraction


def main():
    """
    max sum of digits is 9*20 = 180
    find all partitions of all numbers <= 180
    Too many to enumerate, do something smarter

    Let dp[k][i][j] be number of ordered ways to use j numbers to sum to i and squared sum k.
    Then for a fixed, i, j, dp[i][j], the contribution is
    well the average digit has value i / j
    multiply by the number of ways to place these digits: len choose j
    then multiply by the repunit
    """
    n = 20
    MAXSUM = 9 * n
    MAXSQSUM = 81 * n
    dp = [
        [[0 for _ in range(n + 1)] for _ in range(MAXSUM + 1)]
        for _ in range(MAXSQSUM + 1)
    ]
    dp[0][0][0] = 1
    for i in range(MAXSQSUM):
        for j in range(MAXSUM):
            for k in range(n):
                for d in range(1, 10):
                    d2 = d * d
                    if i + d2 <= MAXSQSUM and j + d <= MAXSUM:
                        dp[i + d2][j + d][k + 1] += dp[i][j][k]

    MOD = 10 ** 9
    repunit = (pow(10, n) - 1) // 9
    print(repunit)

    squares = [x * x for x in range(1, MAXSQSUM + 1)]

    choose = [[1]]
    for i in range(1, n + 1):
        row = [1]
        for j in range(1, i):
            row.append(choose[-1][j - 1] + choose[-1][j])
            if row[-1] >= MOD:
                row[-1] -= MOD

        row.append(1)

        choose.append(row)

    ans = 0
    for sqsum, table in enumerate(dp):
        if sqsum in squares:
            for s, row in enumerate(table):
                for j, ways in enumerate(row):
                    if not ways:
                        continue

                    # print("Contribution of numbers with sq dig sum {} with dig sum {} with {} nonzero digits is {}".format(sqsum, s, j, ways))
                    # print("frac {} repunit {} ways {} choose {}".format(Fraction(s, n), repunit, ways, choose[n][j]))
                    assert (s * repunit * ways * choose[n][j]) % n == 0
                    term = (s * repunit * ways * choose[n][j]) // n
                    # print("Adding", term)
                    ans += term % MOD
                    if ans >= MOD:
                        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
