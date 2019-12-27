q_lo = 50.0
q_hi = 1e16

for _ in range(100):
    q = (q_lo + q_hi) / 2.0

    dp = [0.0 for _ in range(21)]
    dp[0] = 1.0
    for x in range(1, 51):
        p = (1.0 - x / q)
        ndp = [(1.0 - p) * v for v in dp]
        for i in range(20):
            ndp[i + 1] += p * dp[i]

        dp = ndp

    print(q_lo, q_hi, dp[20])
    if dp[20] < 0.02:
        q_hi = q
    else:
        q_lo = q


print(q_lo, q_hi)
