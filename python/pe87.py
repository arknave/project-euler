def gen_primes(n):
    # returns a lit of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return primes

def main():
    primes = gen_primes(7100)

    ans = set()
    CAP = 50000000
    for a in primes:
        v = pow(a, 4)
        if v > CAP:
            v -= pow(a, 4)
            break
        for b in primes:
            v += pow(b, 3)
            if v > CAP:
                v -= pow(b, 3)
                break
            for c in primes:
                v += pow(c, 2)
                if v > CAP:
                    v -= pow(c, 2)
                    break

                ans.add(v)
                v -= pow(c, 2)
            v -= pow(b, 3)
        v -= pow(a, 4)

    print(len(ans))

main()
