import math

def main():
    valid = set()
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if a % 10 == 0 and b % 10 == 0:
                continue

            a0, a1 = a // 10, a % 10
            b0, b1 = b // 10, b % 10
            for aa in [a0, a1]:
                for bb in [b0, b1]:
                    if aa == bb:
                        ax = a0 + a1 - aa
                        bx = b0 + b1 - bb
                        if ax * b == bx * a:
                            valid.add((a, b))
                            break

    print(valid)
    num = 1
    den = 1
    for x, y in valid:
        num *= x
        den *= y

    g = math.gcd(num, den)
    print(num, den)
    print(num // g)
    print(den // g)
main()
