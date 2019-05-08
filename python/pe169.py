"""

How many ways can you write 2^x using no value more than twice??
2^x
2^(x-1) + 2^(x-1)
2^(x-1) + 2^(x-2) + 2^(x-2)
2^(x-1) + 2^(x-2) + 2^(x-3) + 2^(x-3)

so you can stay as your self or kinda smear out to the right
if you smear to the right, you cannot intersect anyone else
so uh
dp[i][j] = using suffix starting from i, are you allowed to be at j?
dp[i][1] = 1 + dp[i][0]
dp[i][0] = dp[next[i]][0] + sum_{k > i, k = 0} dp[k][0]
"""

def f(n):
    bit = 1
    idx = 0
    inds = []
    while bit <= n:
        if (n & bit) > 0:
            inds.append(idx)
        bit <<= 1
        idx += 1

    dp = [[0, 0] for x in inds]
    dp[0][0] = inds[0]
    dp[0][1] = 1 + dp[0][0]

    m = len(dp)
    for i in range(1, m):
        k = inds[i] - inds[i - 1]
        dp[i][0] = (k - 1) * (dp[i - 1][1]) + dp[i - 1][0]
        dp[i][1] = dp[i][0] + dp[i - 1][1]

    return dp[m - 1][1]

print(f(10**25))
