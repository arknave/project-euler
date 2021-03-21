import math

def gen_sieve(n):
    sieve = [0 for _ in range(n + 1)]

    primes = [2]
    for d in range(2, n + 1, 2):
        sieve[d] = 2

    for d in range(3, n + 1, 2):
        if sieve[d] == 0:
            primes.append(d)
            for j in range(d, n + 1, d):
                sieve[j] = d

    return sieve, primes


def factor(x):
    res = []
    for d in range(1, x):
        d2 = d * d
        if d2 > x:
            break
        if x % d == 0:
            res.append(d)
            if x != d2:
                res.append(x // d)
    res.sort()

    return res

def g(x):
    a, b = 1, 1
    n = 1

    while True:
        n += 1
        a, b = a + 7 * b, a + b
        a %= x
        b %= x

        if a == 1 and b == 0:
            return n

def mat_mul(a, b, m):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % m

    return c

def mat_exp(a, e, m):
    res = [[1, 0], [0, 1]]
    while e > 0:
        if e % 2 == 1:
            res = mat_mul(res, a, m)

        a = mat_mul(a, a, m)
        e //= 2

    return res

def guess_g(x, n):
    # See if (1 + sqrt(7))^n = 1 (mod x)
    mat = mat_exp([[1, 7], [1, 1]], n, x)

    return mat == [[1, 0], [0, 1]]

def fast_factor(p):
    f1s = factor(p - 1)
    f2s = factor(p + 1)
    res = [f1 * f2 for f1 in f1s for f2 in f2s]
    res.sort()

    return res


def lcm(a, b):
    return a // math.gcd(a, b) * b

def main():
    # Write a + b sqrt(7) as the vector [a, b]
    # Then multiplying by 1 + sqrt 7 is the matrix
    
    # (a + b sqrt(7)) (1 + sqrt 7)
    # a + b sqrt(7) + a sqrt(7) + 7 b
    # a + 7b + (a + b) sqrt (7)

    """
    1 7
    1 1
    """

    # Now how to solve for a fixed n?
    # Let the above matrix be A
    # A^n [1 1] = [1 0]

    """
    HOWEVER we do have that 

    g(p^k) = p^(k - 1) * g(p)

    I wish I had something like that for multiplication

    Well, we do have that for primes p, q g(p * q) is a factor of (g[p] * g[q])

    Also holds for numbers of the form p, q, r

    For numbers of the form p^2 q, we have that g(p^2 * q) is a factor of (g(p^2) * g(q))

    For a prime p, answer must be a factor of p^2 - 1

    Tenative idea:
    Try each factor of (p^2 - 1) to get all the prime values
    Then for p^e we know it's just p^(e - 1) * g(p)
    Then for anything else prime decompose and try factors???
    This still seems really slow...

    Holy smokes!!!

    We have the following

    for x = p1^e1 p2^e2 ...

    g(x) = lcm(g(p1^e1), g(p2^e2), ...)

    Now the only hard part left is finding factors of (p^2 - 1). However, we know (p^2 - 1) = (p - 1) * (p + 1), so we can actually factor this fast.

    This is where I solved it. However...

    The faster way is to compute the orders for primes more simply. You can go
    step-by step until b = 0. Let the number of steps here be s. Then you know
    every s steps, b = 0. Iterate by s until a = 0, say k times. Then the order
    is k * s.
    """

    n = 1000 * 1000
    sieve, primes = gen_sieve(n)

    # ignore 2 and 3
    primes = primes[2:]

    gs = [0 for _ in range(n + 1)]
    gs[1] = 1

    for p in primes:
        # Note: to do this faster, iterate until b = 0, then find the order of a using steps of size s
        for f in fast_factor(p):
            if guess_g(p, f):
                gs[p] = f
                break

        if p == 7:
            gs[7] = 7

        print(p, gs[p])

        pe = p
        while pe * p <= n:
            gs[pe * p] = p * gs[pe]
            pe *= p

    ans = 0
    for v in range(6, n + 1, 6):
        for d in [-1, 1]:
            x = v + d
            if gs[x] == 0:
                gs[x] = 1
                y = x
                while y > 1:
                    p = sieve[y]
                    pe = 1
                    while y % p == 0:
                        pe *= p
                        y //= p

                    gs[x] = lcm(gs[x], gs[pe])

            ans += gs[x]

    print(ans)


if __name__ == "__main__":
    main()
