import itertools
import math

def g_seq():
    yield 0
    yield 0
    yield 0
    x = 13
    n = 4
    while True:
        yield x
        n += 1
        x += math.gcd(x, n)

def brute(n):
    return list(itertools.islice(g_seq(), 0, n))[-1]

def factor(x):
    yield 1
    yield x
    for d in range(2, x):
        if d * d > x:
            break
        if x % d == 0:
            yield d
            yield x // d

def adj(a, m):
    return (m - (a % m)) % m

def single_steps(n, g):
    return min(adj(n + 1, f) for f in factor(g - n - 1) if adj(n + 1, f) > 0)

def fast_g(cap):
    n = 4
    g = 13
    while n < cap:
        if (step := math.gcd(n + 1, g)) > 1:
            n += 1
            g += step
        else:
            x = min(cap - n, single_steps(n, g))
            n += x
            g += x

    return g

def main():
    """
    print(brute(1000))
    print(brute(1000000))
    seq = list(itertools.islice(g_seq(), 0, 10000))
    dg = [x - y for x, y in zip(seq[1:], seq)]
    print(seq[-1])
    for i, x in enumerate(dg, start=1):
        if x != 1:
            print(i, x)
    """

    print(fast_g(10**15))

if __name__ == "__main__":
    main()
