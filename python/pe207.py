from fractions import Fraction

def p(m, debug=False):
    n = 2
    k = 2
    num, den = 0, 0
    while k <= m:
        if debug:
            print(n, k, bin(n).count('1'))
        num += bin(n).count('1') == 1
        den += 1
        n += 1
        k = n * (n - 1)

    return Fraction(num, den)
    

def solve(a, b):
    n = 2
    k = 2
    num, den = 0, 1
    while True:
        num += bin(n).count('1') == 1
        den += 1

        if Fraction(num, den) < Fraction(a, b):
            return k

        n += 1
        k = n * (n + 1)


def main():
    print(solve(1, 12345))

if __name__ == "__main__":
    main()
