from math import gcd, sqrt

CAP = 1000000000
MAXN = int(sqrt(CAP)) + 3

def main():
    ans = 0
    for n in range(2, MAXN):
        if n % 1000 == 0:
            print(n)
        start = (n & 1) + 1
        for m in range(start, n, 2):
            if gcd(n, m) == 1:
                leg1 = n * n - m * m
                leg2 = 2 * n * m
                hypot = n * n + m * m

                p1 = 2 * (hypot + leg1)
                p2 = 2 * (hypot + leg2)
                if min(p1, p2) > CAP:
                    break

                if p1 <= CAP and abs(2 * leg1 - hypot) == 1:
                    ans += p1
                if p2 <= CAP and abs(2 * leg2 - hypot) == 1:
                    ans += p2
    print(ans)

main()
