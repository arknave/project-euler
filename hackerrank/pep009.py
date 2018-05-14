from math import gcd

MAX_V = 3003
ans = [-1 for _ in range(MAX_V)]
for n in range(1, MAX_V):
    for m in range(1, n):
        if (n + m) % 2 == 0 or gcd(n, m) != 1:
            continue

        leg1 = n * n - m * m
        leg2 = 2 * n * m
        hypot = n * n + m * m
        perim = leg1 + leg2 + hypot
        prod = leg1 * leg2 * hypot
        for k in range(1, MAX_V):
            val = k * perim
            if val > MAX_V:
                break
            ans[val] = max(ans[val], k * k * k * prod)

T = int(input())
for _ in range(T):
    n = int(input())
    print(ans[n])

