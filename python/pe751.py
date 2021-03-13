from decimal import Decimal
from math import floor

def conc(b):
    while True:
        f = floor(b)
        yield f

        b = f * (b - f + 1)

def adapt(b):
    gen = conc(b)
    a = next(gen)
    s = []
    for _ in range(20):
        s.append(str(next(gen)))

    return Decimal(str(a) + "." + "".join(s))


def main():
    # t = Decimal('2.956938891377988')
    t = Decimal(2)
    for _ in range(20):
        nxt = adapt(t)
        print(t, nxt)
        t = nxt

    ans = str(t)
    print(ans[:26], ans[26])

if __name__ == '__main__':
    main()
