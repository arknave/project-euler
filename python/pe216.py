def is_prime(n):
    """Miller Rabin"""
    assert n < 7e18
    if n < 6 or n % 6 not in [1, 5]:
        return n == 2 or n == 3

    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    s = 0
    while ((n - 1) & (1 << s)) == 0:
        s += 1
    d = n >> s
    for a in A:
        p = pow(a % n, d, n)
        i = s
        while p != 1 and p != n - 1 and a % n > 0 and i > 0:
            i -= 1
            p = p * p % n
        if p != n - 1 and i != s:
            return False

    return True


def f(n):
    """
    Count the number of primes of the form 2x^2 - 1 where 1 <= x <= n.

    TODO: This is still too slow, should be able to speed up by checking if
    2x^2 = 1 mod p for several small odd primes p. This is only possible if
    x^2 == (p + 1) / 2 mod p
    """
    ans = 0
    for x in range(1, n + 1):
        if is_prime(2 * x * x - 1):
            ans += 1

    return ans


def main():
    ans = f(50_000_000)
    print(ans)

if __name__ == "__main__":
    main()
