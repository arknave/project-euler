from fractions import Fraction

def solve(d):
    # find the largest n coprime to d such that
    # n / d == 3 / 7
    # 7 * n == 3 * d
    n = 3 * d // 7

    return n

def main():
    best = Fraction(1, 3)
    target = Fraction(3, 7)
    for den in range(4, 1000001):
        num = solve(den)
        f = Fraction(num, den)
        if f > best and f < target:
            best = f

    print(best.numerator, best.denominator)

main()
