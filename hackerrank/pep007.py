MAX_VAL = 500000
sieve = [True for _ in range(MAX_VAL)]
primes = [2]
for d in range(3, MAX_VAL, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d, MAX_VAL, d):
            sieve[j] = False

T = int(input())
for _ in range(T):
    x = int(input())
    print(primes[x - 1])
