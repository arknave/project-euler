from fractions import Fraction

def gen_sieve(n):
    # sieve[n] is the smallest pf that divides n
    sieve = list(range(n))
    for x in range(2, n, 2):
        sieve[x] = 2

    for d in range(3, n, 2):
        if sieve[d] == d:
            for j in range(d * d, n, 2 * d):
                sieve[j] = min(sieve[j], d)

    return sieve

def phi(n, sieve):
    ans = 1

    while sieve[n] != n:
        d = sieve[n]
        a = 1
        while sieve[n] == d:
            a *= d
            n //= d

        ans *= (a - (a // d))

    if n > 1:
        ans *= (n - 1)

    return ans

def main():
    CAP = 1000000 + 1
    s = gen_sieve(CAP)

    ans = sum(phi(n, s) for n in range(2, CAP))
    print(ans)

main()
