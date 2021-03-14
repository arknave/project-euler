def gen_primes(n):
    # returns a list of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(2, n, 2):
        sieve[d] = 2
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return sieve, primes

def solve(n):
    sieve, primes = gen_primes(n + 1)

    num_primes = len(primes)
    ans = (1, 2)
    for i, p in enumerate(primes):
        tot = 0
        used = 0
        for j in range(i, len(primes)):
            tot += primes[j]
            used += 1

            if tot <= n and sieve[tot] == tot:
                ans = max(ans, (used, tot))

    return ans


def main():
    print(100, solve(100))
    print(1000, solve(1000))
    print(1000000, solve(1000000))

if __name__ == "__main__":
    main()
