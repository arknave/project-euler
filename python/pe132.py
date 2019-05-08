# this is guessed
GUESS = int(1e7)
sieve = [(i % 3 != 0 and i % 5 != 0) for i in range(GUESS)]
primes = [7]
for k in range(12, GUESS, 6):
    for d in range(-1, 2, 2):
        v = k + d
        if sieve[v]:
            primes.append(v)
            for j in range(3 * v, GUESS, 2 * v):
                sieve[j] = False

# R(n) = sum 10^k
# R(n) = (10^(k + 1) - 1) / 9
ans = []
k = int(1e9)
for p in primes:
    v = (pow(10, k, p) + (p - 1)) * pow(9, p - 2, p) % p
    if v == 0:
        ans.append(p)
        if len(ans) >= 40:
            break
print(ans)
print(sum(ans))
