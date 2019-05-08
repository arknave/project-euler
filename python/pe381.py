n = int(1e8)

sieve = [True for i in range(n)]
primes = []
for v in range(6, n, 6):
    for d in (v - 1, v + 1):
        if sieve[d]:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = False

def S(p):
    ans = p - 1
    cur = p - 1
    for k in range(2, 6):
        cur = (cur * pow(p - k + 1, p - 2, p)) % p
        ans += cur
    ans %= p
    #print(p, ans)
    return ans

print(sum(S(p) for p in primes))
