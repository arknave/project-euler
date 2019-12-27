# How many triples (a, b, c) are there where (c^2 - 2 * a * b) | c^2
# This means that 2 * a * b | c^2
# This means that 2 * 2 * n * m * (n^2 - m^2) | (n^2 + m^2)

# How many pyth. triples (a, b, c) are there where b - a | c?
# This means that b - a = kc

from math import sqrt, gcd

ans = 0
CAP = int(1.1e4)
MAXP = 100000000

for n in range(1, CAP):
    for m in range(1, n):
        if (n + m) % 2 == 0 or gcd(n, m) != 1:
            continue

        a = n * n - m * m
        b = 2 * n * m
        c = n * n + m * m
        p = a + b + c

        d = abs(b - a)

        if p >= MAXP or c % d != 0:
            continue

        max_scale = (MAXP - 1) // p
        print(a, b, c, max_scale)
        ans += max_scale

print('ans', ans)
