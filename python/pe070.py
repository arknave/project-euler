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

def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))

def main():
    CAP = int(1e7) + 1
    s = gen_sieve(CAP)

    f = Fraction(int(1e8), 1)
    for n in range(2, CAP):
        p = phi(n, s)
        ff = Fraction(n, p)
        if is_perm(n, p) and ff < f:
            print(n, p)
            f = ff

main()
