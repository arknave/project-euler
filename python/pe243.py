import itertools

def gen_sieve(n):
    sieve = list(range(n + 1))
    primes = [2]
    for d in range(2, n, 2):
        sieve[d] = 2

    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return primes, sieve

def phi(x, sieve):
    ans = x
    while x > 1:
        pf = sieve[x]
        ans //= pf
        ans *= pf - 1
        while x % pf == 0:
            x //= pf

    return ans
    
def main():
    # find the smallest x such that 
    # phi(x) / (x - 1) < 15499 / 94744
    # 94744 * phi(x) < (x - 1) * 15499
    # ... just gen 1 at a time until it works?
    # that doesnt work, 10^7 isnt enough
    # should have lots of prime factors...
    # just try prefix products of primes?
    NUM, DEN = 15499, 94744
    # NUM, DEN = 4, 10

    # tweaked these constants a bit to get it to run quickly and accurately
    PRIME_CAP = 30
    MAX_FACT = 12
    primes, sieve = gen_sieve(PRIME_CAP)
    primes = [1] + primes
    ans = float('inf')
    for pf in itertools.combinations_with_replacement(primes, MAX_FACT):
        phi = 1
        n = 1
        for i, p in enumerate(pf):
            phi *= p
            n *= p
            if i > 0 and pf[i - 1] != pf[i]:
                phi //= p
                phi *= p - 1

        if DEN * phi < (n - 1) * NUM:
            ans = min(ans, n)

    print(ans)

main()
