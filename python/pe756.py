from decimal import getcontext, Decimal

import functools
import itertools
import math
import random


@functools.lru_cache()
def choose(n, m):
    assert False
    if m < 0 or m > n:
        return 0

    return math.factorial(n) // math.factorial(m) // math.factorial(n - m)


# P(i, j) probability that index i out of n is chosen as the j-th value out of m
@functools.lru_cache()
def prob(i, j, n, m):
    assert False
    if i == 0 or j == 0:
        return 1.0 if i == j else 0.0

    return choose(i - 1, j - 1) * choose(n - i, m - j) / choose(n, m)


def solve_slow(f, n, m):
    res = 0.0
    for j in range(1, n + 1):
        res += choose(n - j, m - 1) / choose(n, m) * f[j] * j

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            score = f[j] * (j - i)
            # exclude this range, choose m - 2 other points
            p = choose(n - j + i - 1, m - 2) / choose(n, m)
            # print("seg", i, j, p)
            res += p * score

    return res


def solve_fast(f, n, m):
    """
    Main idea: for each interval [i, j], the contribution to the expected value
    is f[j] * j * prob((i, j) in our list)

    The prob is a division of binomial coefficinets that can easily be updated.
    solve in linear time!
    """
    getcontext().prec = 20
    assert len(f) == n + 1
    res = Decimal(0)
    # m / n, [m (n - m)] / [n (n - 1)], [m (n -m) (n - m - 1)] / [n (n - 1) (n - 2)]
    coeff = Decimal(m) / Decimal(n)
    for j in range(1, n + 1):
        # res += choose(n - j, m - 1) / choose(n, m) * f[j] * j
        res += coeff * f[j] * j
        if j < n:
            coeff *= Decimal(n - m - j + 1) / Decimal(n - j)

    # only do the binomial division
    # [m (m - 1)] / [n (n - 1)], [m (m - 1) (n - m)] / [n (n - 1) (n - 2)], [m (m - 1) (n - m) (n - m - 1)] / [n (n - 1) (n - 2) (n - 3)]
    # cur_coeff = (n - 2 choose m - 2) / (n choose m)
    cur_coeff = Decimal(m * (m - 1)) / Decimal(n * (n - 1))
    sum_coeff = cur_coeff
    EPS = 1e-15
    for i in range(1, n):
        # print(i, cur_coeff, sum_coeff)
        if cur_coeff < EPS:
            for j in range(i, n):
                res += f[j + 1]
            break

        res += f[i + 1] * sum_coeff
        if i + 1 < n:
            cur_coeff *= Decimal(n - m - (i - 1)) / Decimal(n - (i + 1))
            sum_coeff += (i + 1) * cur_coeff

    return res


def brute(f, n, m):
    res = 0
    total = 0
    for idxs in itertools.combinations(range(1, n + 1), m):
        cur = 0
        total += 1
        last = 0
        for idx in idxs:
            cur += f[idx] * (idx - last)
            last = idx

        res += cur

    return res / total


def verify():
    while True:
        n, m = random.randint(6, 20), random.randint(2, 5)
        f = [random.randint(1, 100) for _ in range(n + 1)]
        f[0] = 0

        nm = solve_fast(f, n, m)
        exp = brute(f, n, m)
        print(nm, exp)
        EPS = 1e-7
        assert abs(nm - exp) <= EPS
        print("yes")


def gen_phi(n):
    # sieve[n] is the smallest pf that divides n
    phi = list(range(n))
    for d in range(2, n):
        if phi[d] == d:
            for j in range(d, n, d):
                phi[j] //= d
                phi[j] *= d - 1

    return phi


def main():
    n, m = 10000, 100
    n, m = 12345678, 12345
    f = gen_phi(n + 1)

    # print(baby(f, n, m))
    ans = solve_fast(f, n, m)
    print(sum(f), repr(ans))
    print(sum(f) - ans)


if __name__ == "__main__":
    main()
