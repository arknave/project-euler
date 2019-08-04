import math

MAXN = 10000000
MOD = int(1e9 + 87)
# sieve[i] = number of distinct prime factors of i
sieve = [0 for _ in range(MAXN + 1)]
primes = []
for i in range(2, MAXN + 1):
    if sieve[i] == 0:
        primes.append(i)
        for j in range(i, MAXN + 1, i):
            sieve[j] += 1

# What is S(n!)?
# For each divisor d of n!, add 2^w(d)
# How many divisors of n have exactly 0 prime factors? 1. Just 1
# After that it gets tough...

# What are the divisors of n!
# Each exponent for p is the sum floor(n / p) + floor(n / p^2) + .... 
# 2^omega is multiplicative...
# So that means compute these all separately and then multiply

# x 1 2 3 4 5 6
# w 0 1 1 1 1 2

# S(6) = S(2) * S(3) = (2^w(1) + 2^w(2)) * (2^w(1) + 2^w(3)) = (1 + 2)^2 = 9

def s_slow(n):
    res = 0
    for x in range(1, n + 1):
        if n % x == 0:
            res += (1 << sieve[x])

    return res

def s(n):
    # actually s(n!)
    assert n >= primes[0]
    lo = 0
    hi = len(primes)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if primes[mid] <= n:
            lo = mid
        else:
            hi = mid

    res = 1
    for i in range(hi):
        p = primes[i]

        e = 0
        x = p
        while x <= n:
            e += n // x
            x *= p

        if e == 1:
            left = hi - i
            res *= pow(3, left, MOD)
            res %= MOD
            break

        v = 1 + 2 * e
        res *= v
        res %= MOD

    # print('s({}) = {}, slow = {}'.format(n, res, s_slow(math.factorial(n))))
    return res

num_primes = len(primes)
moves = [[] for _ in range(MAXN + 1)]

for idx, p in enumerate(primes):
    x = p
    while x <= MAXN:
        for j in range(x, MAXN + 1, x):
            moves[j].append(idx)
        x *= p

def f(n):
    res = 0
    vals = [1 for _ in range(num_primes)]
    cur = 1
    for i in range(2, n + 1):
        for move in moves[i]:
            cur *= pow(vals[move], MOD - 2, MOD)
            vals[move] += 2
            cur *= vals[move]
            cur %= MOD

        res += cur
        res %= MOD

    return res

print(f(MAXN))
