import math

import pelib


def solve(n, mod):
    """
    What is sum of divisors of n?
    This is a multiplicative function

    sigma(p) = p + 1
    sigma(p^k) = (p^(k + 1) - 1) / (p - 1)

    2017 is prime, so we just need to find primes and prime powers
    where the above is divisible by 2017.

    Can brute force k >= 2.
    For k == 1, p + 1 == 0 (mod 2017).
    Can use a kind of sieve to find primes in O(n / m).

    Then the next step is some kind of PIE to sum the values that are divisible
    by at least one value in the list.
    """

    values = []
    s = math.isqrt(n)
    primes = pelib.gen_primes(s + 1)
    for p in primes:
        x = p * p
        e = 2
        while x <= n:
            assert (x * p - 1) % (p - 1) == 0
            if (x * p - 1) // (p - 1) % mod == 0:
                values.append((x, p))
            e += 1
            x *= p

    # sieve[x] = Mx + M - 1
    sieve_size = (n + mod - 1) // mod
    is_prime = [True] * sieve_size

    for p in primes:
        if p == mod:
            continue
        # Mx + M - 1 = 0 (mod p)
        # Mx = 1 - M
        x = (1 - mod) % p * pow(mod, p - 2, p) % p
        start = x * mod + mod - 1
        for y in range(x, sieve_size, p):
            v = mod * y + mod - 1
            assert v % p == 0
            if v > p:
                is_prime[y] = False

    for x, is_p in enumerate(is_prime):
        if is_p:
            v = mod * x + mod - 1
            values.append((v, v))

    values.sort()
    assert math.prod([x[0] for x in values[:3]]) > n

    def count(x):
        f = n // x
        return x * f * (f + 1) // 2

    ans = 0
    for x, p in values:
        ans += count(x)
        ans -= count(x * p)
        for y, _ in values:
            xy = x * y
            if y >= x or xy > n:
                break
            ans -= count(xy)
            ans += count(xy * p)

    return ans


def main():
    for n, m in [(20, 7), (10**6, 2017), (10**9, 2017), (10**11, 2017)]:
        ans = solve(n, m)
        print(n, m, ans)


if __name__ == "__main__":
    main()
