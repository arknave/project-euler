from math import gcd
import itertools

MAXP = 45
sieve = [0 for _ in range(MAXP)]
primes = []
for i in range(2, MAXP):
    if sieve[i] == 0:
        primes.append(i)
        for j in range(i, MAXP, i):
            sieve[j] = i

y = 1
for p in primes:
    y *= p
x = 13082761331670030
print(x, y)

#primes = [7, 13]

# brute force then recombine using chinese remainder theorem
evidence = []
for p in primes:
    evidence.append([])
    for x in range(1, p):
        if x * x * x % p == 1:
            evidence[-1].append(x)

print(evidence)

# there are six mods and 2 options for each of them
# so 2^6 possibilities
ans = 0

def bezout(n, m):
    assert(gcd(n, m) == 1)
    r0, r1 = n, m
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 > 0:
        q = r0 // r1
        r2 = r0 - q * r1

        assert(r2 == r0 % r1)

        s2 = s0 - q * s1
        t2 = t0 - q * t1

        r0, r1 = r1, r2
        s0, s1 = s1, s2
        t0, t1 = t1, t2

    return s0, t0

def crt(evidence):
    v, m = evidence[0]
    for a, n in evidence[1:]:
        x, y = bezout(n, m)
        assert(n * x + m * y == 1)

        nv = v * n * x + a * m * y + m * n
        nv %= n * m
        while nv < 0:
            nv += n * m

        assert nv % m == v
        assert nv % n == a

        m = m * n
        v = nv % m

    for a, n in evidence:
        assert(v % n == a)
        assert(v * v * v % n == 1)

    return v

for p in itertools.product(*evidence):
    cur = []
    for i, x in enumerate(p):
        cur.append((x, primes[i]))

    v = crt(cur)
    M = 13082761331670030
    print(cur, v, (v * v * v) % M)
    ans += v

print(ans)
