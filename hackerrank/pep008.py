T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    k = int(k)
    ans = 0
    for i in range(n - k):
        prod = 1
        for j in range(i, i + k):
            prod *= int(s[j])
        ans = max(ans, prod)

    print(ans)
