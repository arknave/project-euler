import math

def gen_palindromes(msb):
    def inner(lo, hi, cur):
        if lo > hi:
            yield cur
        else:
            start = int(lo == 1)
            mul = lo if lo == hi else (lo + hi)
            for d in range(start, 10):
                yield from inner(lo * 10, hi // 10, cur + d * mul)

    yield from inner(1, msb, 0)


def palindromes():
    msb = 1
    while True:
        yield from gen_palindromes(msb)
        msb *= 10

def ways(x):
    """Count the number of ways to write x = a^3 + b^2, a, b integers > 1."""

    ans = 0
    a = 2
    a3 = 8
    while a3 < x:
        b2 = x - a3
        b = math.isqrt(b2)
        if b * b == b2:
            ans += 1

        a += 1
        a3 = a * a * a

    return ans

found = []
for p in palindromes():
    if ways(p) == 4:
        found.append(p)
    if len(found) == 5:
        break

print(found)
print(sum(found))

