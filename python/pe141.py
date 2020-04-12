from math import gcd, sqrt

def main():
    # each series is:
    # x * b / a, x, x * a / b
    # (a, b) = 1
    # both a and b have to divide x

    # r = x
    # x^2 + x is a perfect square. I think this cannot happen?
    # That would mean both x and x + 1 are factors, so if it were square, the
    # sqrt would be between, which is impossible

    # r = x * a / b (other case is symmetric)
    # x^2 * b / a + x * a / b
    # (x^2 * b^2 + x * a^2) / ab = n^2
    # x^2 * b^2 + x * a^2 = n^2 ab
    # x (x b^2 + a^2) = n^2 a b
    
    # other note: product of the ends equals the middle squared

    MAXN = 1000000
    factors = [[] for _ in range(MAXN + 1)]
    for d in range(1, MAXN + 1):
        for n in range(d, MAXN + 1, d):
            factors[n].append(d)

    ans = 0
    for x in range(1, MAXN):
        for b in factors[x]:
            for a in factors[x]:
                if b == a:
                    break
                if gcd(a, b) != 1:
                    continue
                r = x * a // b
                d = x * b // a
                if r >= max(x, d):
                    break

                num = x * x * b * b + x * a * a
                den = a * b
                n2 = num // den
                n = int(sqrt(n2))
                if n2 <= MAXN * MAXN and n * n == n2:
                    ans += n2

    print(ans)

if __name__ == '__main__':
    main()
