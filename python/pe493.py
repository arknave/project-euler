dp = [0.0 for _ in range(8)]
dp[0] = 1.0

for i in range(20):
    rem = 70 - i
    ndp = [0.0 for _ in range(8)]
    for j in range(8):
        used_dupes = 70 - rem - j
        ndp[j] += dp[j] * (9 * j - used_dupes) / rem
        if j + 1 <= 7:
            ndp[j + 1] += dp[j] * (10 * (7 - j)) / rem

    dp = ndp
    print(dp)

print(sum(i * p for i, p in enumerate(dp)))
