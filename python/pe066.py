from math import sqrt

def solve(n):
    m = 0
    d = 1
    a0 = a = int(sqrt(n))
    h1, h2 = 0, 1
    k1, k2 = 1, 0

    while True:
        h1, h2 = h2, a * h2 + h1
        k1, k2 = k2, a * k2 + k1

        if d == 0:
            return 0
        m = d * a - m
        d = (n - m * m) // d

        if d == 0:
            return 0

        a = (a0 + m) // d

        if h2 * h2 - n * k2 * k2 == 1:
            return h2

def main():
    """
    The problem wants to find the minimal x for each D such that
    x^2 - D y^2 = 1
    x^2 - 1 = D y^2
    D divides x^2 - 1, so D divides x - 1 or x + 1

    (x - 1)(x + 1) - D y^2 = 0
    """

    biggest = (0, 0)
    for d in range(2, 1000):
        cur = (solve(d), d)
        if cur > biggest:
            biggest = cur

    print(biggest)

main()
