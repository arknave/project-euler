from fractions import Fraction
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(a):
    if len(a) == 1:
        return a

    n = len(a)
    s = set()
    for k in range(1, n):
        left = a[:k]
        right = a[k:]
        for l in solve(left):
            for r in solve(right):
                s.add(l + r)
                s.add(l - r)
                s.add(l * r)
                if r != 0:
                    s.add(Fraction(l, r))
    return s

tot = set()
for mask in range(1 << 8):
    a = [1]
    for d in range(2, 10):
        if (mask & (1 << (d - 2))) > 0:
            a[-1] = a[-1] * 10 + d
        else:
            a.append(d)
    for x in solve(tuple(a)):
        if x.denominator == 1 and x > 0:
            tot.add(x)

print(sum(tot))
