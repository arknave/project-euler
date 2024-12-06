"""
a(2n) = 2a(n)
a(2n + 1) = a(n) - 3a(n + 1)

s(2n) = s(2n - 1) + 2a(n)
s(2n + 1) = s(2n) + a(n) - 3a(n + 1)

s(2n) = s(2(n - 1) + 1) + 2a(n)
s(2n) = s(2(n - 1)) + a(n - 1) - 3a(n) + 2a(n)
s(2n) = s(2(n - 1)) + a(n - 1) - a(n)
s(2n) = s(2(n - 2)) + a(n - 2) - a(n)

s(2n + 1) = s(2n) + a(n) - 3a(n + 1)
s(2n + 1) = s(2n - 1) + a(2n) + a(n) - 3a(n + 1)
s(2n + 1) = s(2n - 1) + 2a(n) + a(n) - 3a(n + 1)
s(2n + 1) = s(2n - 1) + 3a(n) - 3a(n + 1)
s(2n + 1) = s(2(n - 1) + 1) + 3a(n) - 3a(n + 1)
s(2n + 1) = s(2(n - 2) + 1) + 3a(n - 1) - 3a(n + 1)

s(2n) = s(2) + a(1) - a(n)
"""

import functools

@functools.cache
def a(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * a(n // 2)
    else:
        return a(n // 2) - 3 * a(n // 2 + 1)

@functools.cache
def s(n):
    if n == 1:
        return 1

    if n <= 5:
        return sum(a(x) for x in range(1, n + 1))

    if n % 2 == 0:
        return s(2) + a(1) - a(n // 2)
    else:
        return a(n) + s(n - 1)

print(10, s(10))
print(10**12, s(10**12))
