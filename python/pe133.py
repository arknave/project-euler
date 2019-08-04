MAXN = 100000
sieve = [0 for _ in range(MAXN + 1)]
primes = []
for i in range(2, MAXN + 1):
    if sieve[i] == 0:
        primes.append(i)
        for j in range(i, MAXN + 1, i):
            sieve[j] += 1

ans = 0
for p in primes:
    if p < 7:
        continue
    phi = p - 1
    old = -1
    for k in range(1, 100):
        v = pow(10, pow(10, k, phi), p)
        if v == 1:
            print(p, k)
            ans += p
            break
        if v == old:
            break
        old = v

print(ans)
print(sum(primes) - ans)
