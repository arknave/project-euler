import math

# x^3 = n^2p + n^3
# x^3 = n^2(p + n)
# x^3 / n^2 = (p + n)

CAP = int(1e6)
sieve = [i % 2 == 1 for i in range(CAP)]
primes = [2]
for d in range(3, CAP, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d * d, CAP, 2 * d):
            sieve[j] = False

"""
for p in primes:
    for n in range(1, CAP):
        if (n * n * (n + p)) in cubes:
            print(p, n)
            break
"""

"""
Table:
p n
7 1
19 8
37 27
61 64
127 216
271 729

First few are differences of two cubes
7 = 2^3 - 1^3
19 = 3^3 - 2^3
37 = 4^3 - 3^3
61 = 5^3 - 4^3
127 = is not the difference of two cubes. SAD

Seems to only work n is a cube though.
"""

ans = 0
last = 1
for p in primes:
    for x in range(last, max(2 * last, 100)):
        v = x**9 + x**6 * p
        c = int(v**(1/3.0))
        found = False
        for y in range(c-1, c+2):
            if y * y * y == v:
                print(p, x)
                last = x
                ans += 1
                found = True
                break
        if found:
            break

print(ans)
