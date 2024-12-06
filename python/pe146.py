import math

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


def is_prime(n):
    assert n < 7e18
    if n < 10:
        return n in [2, 3, 5, 7]
    if n % 6 not in [1, 5]:
        return False

    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    s = 0
    while ((n - 1) & (1 << s)) == 0:
        s += 1
    d = n >> s
    for a in A:
        p = pow(a%n, d, n)
        i = s
        while p != 1 and p != n - 1 and a % n > 0 and i > 0:
            i -= 1
            p = p * p % n
        if p != n - 1 and i != s:
            return False

    return True


def f(N):
    """Find the sum of all n <= N where

    n^2 + 1, n^2 + 3, n^2 + 7, n^2 + 9, n^2 + 13, n^2 + 27

    are consecutive primes.

    Not all primes >= 5 are of the form 6k +- 1. This is interesting because it
    means that n^2 + 2 has to be divisible by 6, n^2 = 4 (mod 6), so n = 2 or 4 (mod 6).
    
    We can generalize this, and the more primes we use, the better ratio we achieve
    """
    base = 8
    primes = gen_primes(N + 10)
    base_primes = primes[:base]
    assert len(base_primes) == base
    m = math.prod(base_primes)

    ks = [1, 3, 7, 9, 13, 27]
    rs = []
    for r in range(m):
        r2 = r * r
        if all(((r2 + k) % m) % b != 0 for b in base_primes for k in ks):
            rs.append(r)

    print(m, len(rs), len(rs) / m)
    should_prime = [False for _ in range(28)]
    for k in ks:
        should_prime[k] = True

    ans = 0
    for nb in range(0, N + 1, m):
        for r in rs:
            n = nb + r
            if n > N:
                break

            n2 = n * n
            if all(is_prime(n2 + k) == should_prime[k] for k in range(1, 28, 2)):
                ans += n

    return ans


def main():
    ans = f(150_000_000)
    print(ans)

if __name__ == "__main__":
    main()
