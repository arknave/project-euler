from functools import lru_cache
from fractions import Fraction
import itertools

ops = [
    (lambda x, y: x + y, lambda x, y: True),
    (lambda x, y: x - y, lambda x, y: True),
    (lambda x, y: x * y, lambda x, y: True),
    (lambda x, y: x / y, lambda x, y: y != 0)
]

def split(s):
    n = len(s)
    cap = (1 << n) - 1
    for mask in range(1, cap):
        a, b = [], []
        for i in range(n):
            if (mask & (1 << i)) > 0:
                a.append(s[i])
            else:
                b.append(s[i])
        yield tuple(a), tuple(b)

def solve(s):
    if len(s) == 1:
        yield s[0]
        return

    seen = set()
    for left, right in split(s):
        for x in solve(left):
            for y in solve(right):
                for op, pred in ops:
                    if not pred(x, y):
                        continue

                    v = op(x, y)
                    if v not in seen:
                        seen.add(v)
                        # print(left, right, x, y, v)
                        yield v

def score(s):
    x = Fraction(1, 1)
    while x in s:
        x += 1

    return int(x) - 1

def main():
    best_score = 0
    best = (1, 2, 3, 4)

    for combo in itertools.combinations(range(0, 10), 4):
        inp = tuple(map(Fraction, combo))
        made = set()
        for v in solve(inp):
            made.add(v)
        s = score(made)

        if s > best_score:
            best_score = s
            best = combo
            print(best, best_score)

    print(best_score)
    print(best)

main()
