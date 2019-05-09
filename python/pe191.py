# dp[i][j][k] = number of strings of length i that end in j As and have k Lates

dp = [[[0, 0] for _ in range(3)] for _ in range(32)]
dp[0][0][0] = 1
for i in range(30):
    for j in range(3):
        for k in range(2):
            # end with an O
            dp[i + 1][0][k] += dp[i][j][k]
            # end with an A
            if j < 2:
                dp[i + 1][j + 1][k] += dp[i][j][k]
            # end with an L
            if k < 1:
                dp[i + 1][0][k + 1] += dp[i][j][k]

def f(n):
    return sum(map(sum, dp[n]))

for i in range(31):
    print(i, f(i))
