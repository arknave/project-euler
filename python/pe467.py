import math

def dig_root(n):
    while n >= 10:
        x = 0
        while n:
            x += n % 10
            n //= 10
        n = x

    return n


def gen_sieve(n):
    sieve = [False for _ in range(n)]

    for d in range(2, n):
        if not sieve[d]:
            for j in range(d + d, n, d):
                sieve[j] = True

    return sieve


def superseq(s, t):
    n = len(s)
    assert len(t) == n

    # dp[i][j[ len of shortest superseq of s[:i] and t[:j]
    dp = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[0][i] = dp[i][0] = i

    for i in range(n + 1):
        for j in range(n + 1):
            if i + 1 <= n:
                dp[i + 1][j] = min(dp[i + 1][j], 1 + dp[i][j])
            if j + 1 <= n:
                dp[i][j + 1] = min(dp[i][j + 1], 1 + dp[i][j])
            if i + 1 <= n and j + 1 <= n and s[i] == t[j]:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], 1 + dp[i][j])

    res = []
    x, y = n, n
    while x > 0 or y > 0:
        opts = []
        if x > 0 and y > 0 and s[x - 1] == t[y - 1] and dp[x - 1][y - 1] + 1 == dp[x][y]:
            opts.append((s[x - 1], -1, -1))
        if x > 0 and dp[x - 1][y] + 1 == dp[x][y]:
            opts.append((s[x - 1], -1, 0))
        if y > 0 and dp[x][y - 1] + 1 == dp[x][y]:
            opts.append((t[y - 1], 0, -1))

        v, dx, dy = min(opts)
        x += dx
        y += dy
        res.append(v)

    return res


def main():
    MAX_VAL = 105000
    sieve = gen_sieve(MAX_VAL)
    primes, comps = [], []
    for x in range(2, MAX_VAL):
        if sieve[x]:
            comps.append(x)
        else:
            primes.append(x)

    n = 10000
    assert len(comps) >= n and len(primes) >= n
    comps = comps[:n]
    primes = primes[:n]

    s = [dig_root(x) for x in primes]
    t = [dig_root(x) for x in comps]

    res = superseq(s[::-1], t[::-1])

    ans = 0
    p = 1
    MOD = int(1e9 + 7)
    for c in reversed(res):
        ans += p * c % MOD
        if ans >= MOD:
            ans -= MOD
        p = p * 10 % MOD

    print(ans)


if __name__ == "__main__":
    main()
