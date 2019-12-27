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

primes = gen_primes(1000000)
stk = [(1, 0)]
CAP = int(input())
ans = 0
while stk:
    x, pi = stk.pop()
    if pi >= len(primes):
        ans += CAP // x
        continue

    v = x * (primes[pi] ** 3)
    if v > CAP:
        ans += CAP // x
        continue

    stk.append((x, pi + 1))
    while v <= CAP:
        stk.append((v, pi + 1))
        v *= primes[pi]

print('ans', ans)
