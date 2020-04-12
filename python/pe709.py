MOD = 1020202009
GOAL = 24680
INV2 = (MOD + 1) // 2

fact = [1]

for i in range(1, GOAL + 1):
    fact.append(fact[-1] * i % MOD)

tcaf = [pow(x, MOD - 2, MOD) for x in fact]

dp = [1, 1]

for n in range(1, GOAL):
    res = 0
    for k in range(0, n + 1):
        res += fact[n] * tcaf[k] % MOD * tcaf[n - k] % MOD * dp[k] % MOD * dp[n - k] % MOD
        if res >= MOD:
            res -= MOD
    dp.append(res * INV2 % MOD)

print(dp[-1])
