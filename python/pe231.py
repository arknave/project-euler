n = 20000000
k = 15000000

sieve = [i % 2 == 1 for i in range(n + 1)]
primes = [2]
for d in range(3, n + 1, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d * d, n + 1, 2 * d):
            sieve[j] = False

def count(n, p):
    ans = 0
    d = p
    while d <= n:
        ans += (n // d)
        d *= p
    return ans

ans = 0
for p in primes:
    exp = count(n, p) - count(k, p) - count(n - k, p)
    ans += p * exp 

print(ans)
