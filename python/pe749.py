INF = 10**17
MAXK = 56

def dig_sum(x, k):
    """Return the sum of the k-th powers of the digits of x"""
    v = 0
    while x > 0:
        d = x % 10
        v += d ** k
        x //= 10

        if v >= INF:
            return INF

    return v


def nps(x):
    """Is x a near power sum?"""
    for k in range(1, MAXK):
        ds = dig_sum(x, k)
        if ds == x - 1 or ds == x + 1:
            return True
        if ds > x + 1:
            break

    return False


def f(d, n):
    """Yields all lists of length n with digits in the range [0..d]"""
    if n == 0 or d <= 0:
        yield []
        return

    for k in range(n + 1):
        for l in f(d - 1, n - k):
            yield [d]*k + l


def s(d):
    cap = 10 ** d
    sums = set()
    for l in f(9, d):
        for k in range(1, MAXK):
            x = sum(x ** k for x in l)
            if x - 1 >= cap:
                break

            sums.add(x)

    print(d, len(sums))
    ans = set()
    for x in sums:
        for y in [x - 1, x, x + 1]:
            if 0 <= y < cap and nps(y):
                ans.add(y)

    # print(ans)
    return sum(ans)


def main():
    for x in [2, 6, 16]:
        print(x, s(x))


if __name__ == "__main__":
    main()
