import itertools
from fractions import Fraction

def values():
    yield 2
    k = 2
    while True:
        yield 1
        yield k
        yield 1

        k += 2

def main():
    parts = list(itertools.islice(values(), 100))

    f = Fraction(0)
    print(f)
    for value in reversed(parts):
        f = 1 / (f + value)
        print(f)

    f = 1 / f
    print(sum(map(int, str(f.numerator))))

main()
