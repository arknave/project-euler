# number of palindromic tuples with at least one two
# 3 cases:
# 1 even length
# 2 odd length center 2
# 3 odd length not center 2

# case 1:
# if n is odd, impossible
# normally just stars and bars on n / 2 to count number of partitions
# how do you handle the 2? IE on the number of twos?
# case 1: number of ways including at least 1 two = (n/2 choose 1) sab(n/2 - 2) - (n/2 choose 2) sab(n/2 - 4) + ...

# case 2:
# just sab on n - 2 / 2. also impossible if n is odd 

# case 3:
# iterate on middle value and sum i guess

"""
choose = [[1], [1, 1]]
for i in range(2, 50):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = choose[-1][j - 1] + choose[-1][j]

    choose.append(row)

def sab(n, k):
    if k > n or k <= 0 or n <= 0:
        return 0
    return choose[n - 1][k - 1]
"""

# dp[i][0] = number of partitions with no twos
# dp[i][1] = number of partitions with at least 1 2

M = 1000000
dp = [(1, 0), (1, 0)]
p = [0, 0]
ans = [0, 0]
sum0 = 2
sum1 = 0
i = 2
while i < 42 or ans[-1] != 0:
    x = (sum0 - dp[i - 2][0]) % M
    y = (sum1 + dp[i - 2][0]) % M
    sum0 += x
    sum1 += y
    sum0 %= M
    sum1 %= M
    dp.append((x % M, y % M))

    cur = 0
    if i % 2 == 0:
        h = i // 2
        cur += dp[h][1] + dp[h - 1][0] + dp[h - 1][1]
        # cur += sum(dp[(i - x) // 2][1] for x in range(4, i, 2))
        cur += p[i // 2 - 2]
        cur %= M
    else:
        # cur = sum(dp[(i - x) // 2][1] for x in range(1, i, 2))
        cur = p[i // 2]
        cur %= M

    ans.append(cur)
    p.append((p[-1] + dp[i][1]) % M)
    i += 1
    # print(i, dp[-1], ans[-1], p[-1])
    if i % 1000 == 0:
        print(i)

print(i - 1)

"""
def t(n):
    # case 1
    ans = 0
    if n % 2 == 0:
        # print('case 1', dp[n // 2][1])
        ans += dp[n // 2][1]

    ans %= M

    # case 2
    if n % 2 == 0:
        # print('case 2', dp[(n - 2) // 2][0] + dp[(n - 2) // 2][1])
        ans += dp[(n - 2) // 2][0] + dp[(n - 2) // 2][1]

    ans %= M
    for mid in range(n % 2, n, 2):
        if mid != 0 and mid != 2:
            # print('case 3', mid, dp[(n - mid) // 2][1])
            ans += dp[(n - mid) // 2][1]

    ans %= M
    return ans
"""
