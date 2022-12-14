from math import isqrt

def digits(x, b):
    while x > 0:
        yield x % b
        x //= b


def solve(b, d):
    # find a small x such that x^2 has d as a digit in base b
    # units digit: solve x^2 = d (mod b)
    # every other digit: solve floor(x^2 / b^i) = aM + d for increasing a, i
    # Theory: only have to check last two digits

    """
    floor(x^2 / b^i) = k
    x^2 / b^i >= k
    x^2 >= b^i k
    x >= sqrt(b^i k)
    """

    opts = []
    # first, the units digit
    # because b % 4 == 3, this has an easy closed form
    assert b % 4 == 3
    r = pow(d, (b + 1) // 4, b)
    if r * r % b == d:
        opts.append(r)
    r = -r % b
    if r * r % b == d:
        opts.append(r)

    opts.sort()

    lead = 0
    b2 = b * b
    term = b * d
    while not opts or opts[-1] * opts[-1] > term:
        x = isqrt(term)
        while x * x < term:
            x += 1
        if (x * x // b) % b == d:
            opts.append(x)
            break

        lead += 1
        term += b2

    # now try b^2 just for funsies
    # x^2 = d b^2 + ....
    x = isqrt(d * b * b)
    while x * x < d * b * b:
        x += 1

    if x * x // b // b == d:
        opts.append(x)

    return opts


def main():
    M = 1000000007
    ans = 0
    for d in range(1, 100000 + 1):
        v = M - d
        opts = solve(M, v)
        s = min(opts)
        assert v in list(digits(s * s, M)), (v, s, opts)
        ans += s

    print(ans)

if __name__ == '__main__':
    main()
