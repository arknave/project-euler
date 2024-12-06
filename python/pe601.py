import functools
import math

def euclid(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = euclid(b, a % b)
    return g, x, y - (a // b) * x

def crt(p1, p2):
    a, m = p1
    b, n = p2
    if a is None or b is None:
        return (None, None)

    d = math.gcd(m, n)
    if (a - b) % d != 0:
        return (None, None)

    g, x, y = euclid(m // d, n // d)
    l = (a - b) // d
    ret_mod = m // d * n
    l %= ret_mod
    ret = b + n * l * y
    ret %= ret_mod

    return (ret, ret_mod)

def count(n, x, m):
    """
    How many integers < n are equivalent to x (mod m)?
    """
    ans = n // m 
    if n > x and x < n % m:
        ans += 1

    print(f"count({n=}, {x=}, {m=}) = {ans}")
    return ans

def p(s, n):
    """
    How many integers in (1, n) have streak(x) = s?
    """
    facts = [(1, i) for i in range(1, s + 1)]
    res1 = functools.reduce(crt, facts)
    res2 = crt(res1, (1, s + 1))

    return count(n, *res1) - count(n, *res2)

def streak(x):
    k = 1
    while (x + k) % (k + 1) == 0:
        k += 1

    return k

def brute(s, n):
    ans = 0
    for x in range(2, n):
        if streak(x) == s:
            ans += 1

    return ans

def main():
    # s(n) is the smallest k where (n + k) is not divisible by k + 1
    # equivalently,
    # x = 1 (mod 2)
    # x = 1 (mod 3)
    # x = 1 (mod 4)
    # ...
    # x != k - 1 (mod k)

    # CRT of the above gives an overestimate
    # can use PIE for exact s

    assert streak(13) == 4
    assert streak(120) == 1

    assert p(3, 14) == 1
    assert brute(3, 14) == 1

    assert p(6, 10**6) == 14286
    assert brute(6, 10**6) == 14286

    for i in range(2, 10):
        have = p(i, 4**i)
        b = brute(i, 4**i)
        assert have == b, (have, b)

    # -1 because this is counting 1 for some reason...
    ans = sum(p(i, 4**i) for i in range(1, 32)) - 1
    print(ans)

if __name__ == "__main__":
    main()
