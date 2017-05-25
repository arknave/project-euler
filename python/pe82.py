import copy

def main():
    n = 80
    data = [list(map(int, input().split(','))) for _ in range(n)]
    dp = copy.deepcopy(data)

    for j in range(1, n):
        for i in range(n):
            # 3 ways to get into a cell
            # 1. from the left
            dp[i][j] = data[i][j] + dp[i][j - 1]
            # 2. or above
            if i > 0:
                dp[i][j] = min(dp[i][j], data[i][j] + dp[i - 1][j])
        for i in range(n - 1, -1, -1):
            # 3. or below
            if i < n - 1:
                dp[i][j] = min(dp[i][j], data[i][j] + dp[i + 1][j])

    ans = min(dp[x][-1] for x in range(n))
    print(ans)

main()
