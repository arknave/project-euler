CAP = 10000
sieve = [i % 2 == 1 for i in range(CAP)]
primes = [2]
for d in range(3, CAP, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d * d, CAP, 2 * d):
            sieve[j] = False

def is_prime(n):
    if n < CAP:
        return sieve[n]
    return all(n % p != 0 for p in primes)

m = len(primes)
ans = 0
M = int(1e8)
for p in primes:
    for j in range(p * p, M, p):
        if is_prime(j // p):
            ans += 1

print(ans)
