import bisect

MAX_VAL = 1000000
sieve = [True for _ in range(MAX_VAL)]
primes = [2]
for d in range(3, MAX_VAL, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d * d, MAX_VAL, 2 * d):
            sieve[j] = False

prime_sum = list(primes)
for i in range(1, len(primes)):
    prime_sum[i] += prime_sum[i - 1]

T = int(input())
for _ in range(T):
    n = int(input())
    idx = bisect.bisect(primes, n)
    print(prime_sum[idx - 1])
