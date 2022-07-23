import math

def main():
    """
    It feels pretty intuitive that a < c. Then we have a * b = c * d, a + b == c + d + 1.

    b = c + d + 1 - a
    a(c + d + 1 - a) = cd
    ac + ad - a - a^2 = cd
    d = (ac + a - a^2) / (c - a)
    Then b = cd / a

    Let's fix the denominator: c - a
    It feels like the denominator has to divide a and c, but I cannot prove it
    Holds up to 1e6, so probably holds up to 1e14?
    """
    s = set()
    CAP = 10**14
    SQRT = int(math.sqrt(CAP)) + 1
    RT4 = int(math.sqrt(SQRT)) + 2
    for den in range(1, RT4 + 1):
        print(den, RT4)
        for a in range(den, SQRT + 1, den):
            c = a + den
            num = a * c + a - a * a
            assert num % den == 0
            d = num // den
            assert c * d % a == 0
            b = c * d // a
            n = a * b
            assert n == c * d
            assert a % den == 0
            assert c % den == 0
            assert a + b == c + d + 1
            if n <= CAP:
                s.add(n)
            else:
                break

    print(len(s))

if __name__ == "__main__":
    main()
