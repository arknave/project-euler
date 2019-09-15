MAXN = 10000000
# sieve[i] = number of distinct prime factors of i
sieve = [0 for _ in range(MAXN + 1)]
primes = []
for i in range(2, MAXN + 1):
    if sieve[i] == 0:
        primes.append(i)
        for j in range(i, MAXN + 1, i):
            sieve[j] += 1

def is_prime(n):
    if n < 2:
        return False
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False

    return True

dp = [(0, 0)]
ans = 0
for _ in range(13):
    ndp = []
    for x, s in dp:
        for d in range(10):
            if x == 0 and d == 0:
                continue

            nx = 10 * x + d
            ns = s + d
            if nx % ns == 0:
                ndp.append((nx, ns))

    dp = ndp
    print(len(dp))
    for x, s in dp:
        for d in [1, 3, 7, 9]:
            if is_prime(10 * x + d) and is_prime(x // s):
                ans += 10 * x + d

print(ans)
