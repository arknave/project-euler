CAP = 10000
sieve = [i % 2 == 1 for i in range(CAP)]
primes = [2]
for d in range(3, CAP, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d * d, CAP, 2 * d):
            sieve[j] = False

f = {}
for p in primes:
    if p < 1000:
        continue
    hsh = ''.join(sorted(str(p)))
    if hsh not in f:
        f[hsh] = []
    f[hsh].append(p)
    m = len(f[hsh])
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if f[hsh][j] - f[hsh][i] == f[hsh][k] - f[hsh][j]:
                    print(f[hsh][i], f[hsh][j], f[hsh][k])
