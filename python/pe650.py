from math import factorial

MAXN = 20000
MOD = int(1e9 + 7)
# sieve[i] = number of distinct prime factors of i
sieve = [-1 for _ in range(MAXN + 1)]
primes = []
for i in range(2, MAXN + 1):
    if sieve[i] == -1:
        for j in range(i, MAXN + 1, i):
            sieve[j] = len(primes)
        primes.append(i)

num_primes = len(primes)
def s(n):
    dp = [[0 for _ in primes]]
    for i in range(1, n + 1):
        dp.append(list(dp[i - 1]))
        v = i
        while v > 1:
            idx = sieve[v]
            p = primes[idx]
            dp[i][idx] += 1
            v //= p

    for i in range(1, n + 1):
        for j in range(num_primes):
            dp[i][j] += dp[i - 1][j]

    ans = 0
    for i in range(1, n + 1):
        cur = 1
        for j, p in enumerate(primes):
            if p > i:
                break

            occ = (dp[i][j] - dp[i - 1][j]) * (i + 1) - 2 * dp[i][j]
            cur *= (pow(p, occ + 1, MOD) + MOD - 1) * pow(p - 1, MOD - 2, MOD) % MOD
            cur %= MOD

        ans += cur
        ans %= MOD

    return ans

print(s(5))
print(s(10))
print(s(100))
print(s(20000))
