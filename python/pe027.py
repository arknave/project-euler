def gen_primes(n):
    # returns a lit of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return set(primes)

MAXN = 1000
CAP = MAXN * MAXN + 1000 * MAXN + 1000

primes = gen_primes(CAP + 1)

def score(a, b):
    n = 0
    while True:
        # (n + 1)^2 + a (n + 1) + b - n^2 - an - b
        # 2n + 1 + a
        v = n * n + a * n + b
        if v not in primes:
            break

        n += 1
    return n

best = -1
for a in range(-1000, 1001):
    for b in range(2, 1001):
        if b not in primes:
            continue
        cur = score(a, b)
        if cur > best:
            best = cur
            ans = a * b

print(ans)
