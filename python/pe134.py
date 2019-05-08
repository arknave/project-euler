# x * 10^k = -p1 (mod p2)
# x = -p1 * 10^-k(mod p2)
CAP = 1000000 + 100
sieve = [True for _ in range(CAP)]
primes = []
for k in range(6, CAP, 6):
    for d in range(-1, 2, 2):
        v = k + d
        if sieve[v]:
            primes.append(v)
            for j in range(3 * v, CAP, 2 * v):
                sieve[j] = False

ans = 0
k = 10
for i, p1 in enumerate(primes):
    if not (5 <= p1 <= CAP - 100):
        break

    p2 = primes[i + 1]
    while k <= p1:
        k *= 10
    x = (p2 - p1) * pow(k % p2, p2 - 2, p2)
    x %= p2
    s = x * k + p1
    assert s % p2 == 0
    if p2 < 100:
        print(p1, p2, s)
    ans += s

print(ans)
