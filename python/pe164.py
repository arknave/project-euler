dp = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(21)]
for a in range(1, 10):
    for b in range(10):
        dp[2][a][b] += 1

for k in range(3, 21):
    for a in range(10):
        for b in range(10):
            for c in range(10):
                if a + b + c < 10:
                    dp[k][b][c] += dp[k - 1][a][b]

print(sum(map(sum, dp[20])))
