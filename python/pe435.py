import functools
import math

def euclid(a, b):
    """
    Solves ax + by = gcd(a, b)

    returns gcd, x, y
    """
    if b == 0:
        return a, 1, 0
    d, y, x = euclid(b, a % b)

    return d, x, y - (a // b) * x


def solve_linear(a, b, m):
    """
    solve ax = b (mod m)
    """
    assert 0 <= a < m
    assert 0 <= b < m
    if a == 0:
        return 0 if b == 0 else None

    g, x, y = euclid(a, m)
    if b % g != 0:
        return None

    a //= g
    b //= g
    m //= g

    res = b * x % m

    return res


def brute(n, x):
    a, b = 0, 1
    ans = 0
    for i in range(1, n + 1):
        a, b = b, a + b
        ans += a * x**i

    return ans


@functools.cache
def fib(n, mod=None):
    if n <= 1:
        return n

    fa = fib((n + 1) // 2, mod)
    fb = fib((n - 1) // 2, mod)
    if n % 2 == 1:
        ans = fa**2 + fb**2
    else:
        ans = (2 * fb + fa) * fa

    if mod:
        return ans % mod
    else:
        return ans


def poly_slow(n, x):
    a = fib(n)
    b = fib(n + 1)
    num = x - b * x**(n + 1) - a * x**(n + 2)
    den = 1 - x - x**2

    assert num % den == 0
    return num // den


def poly_mod(n, x, mod):
    a = fib(n, mod)
    b = fib(n + 1, mod)
    num = x - b * pow(x, n + 1, mod) - a * pow(x, n + 2, mod)
    den = 1 - x - x**2

    return solve_linear(den % mod, num % mod, mod)


def main():
    mod = math.factorial(15)

    print(sum(poly_mod(10**15, x, mod * abs(x**2 + x - 1)) % mod for x in range(101)) % mod)

if __name__ == "__main__":
    main()
