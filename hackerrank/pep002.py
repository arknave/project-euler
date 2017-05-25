import sys

def solve(n):
    a, b = 1, 2
    ans = 0
    while b <= n:
        if b % 2 == 0:
            ans += b
        a, b = b, a + b
        
    return ans

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
