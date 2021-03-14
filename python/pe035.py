def gen_primes(n):
    # returns a list of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return primes

primes = set(gen_primes(1000000))

ans = 0
for x in primes:
    if x <= 10:
        ans += 1
        continue

    s = str(x)
    rots = [int(s[i:] + s[:i]) for i in range(len(s))]
    if all(p in primes for p in rots):
        ans += 1

print(ans)
