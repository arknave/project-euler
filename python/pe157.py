import math

"""
1/a + 1/b = p/n
na + nb = abp
0 = abp^2 - nap - nbp
n^2 = abp^2 - nap - nbp + n^2
n^2 = (pa - n)(pb - n)

Find all factors of n^2, say the pair is f and g. Then we have
pa - n = f
pb - n = g
pa = f + n
pb = g + n
p | gcd(f + n, g + n)

brute force from here?
"""


def count_divs(n):
    ans = 0
    for d in range(1, n):
        if d * d > n:
            break
        if n % d == 0:
            if d * d == n:
                ans += 1
            else:
                ans += 2

    return ans


def solve(k):
    n = pow(10, k)
    n2 = n * n
    ans = 0
    for a in range(k + k + 1):
        for b in range(k + k + 1):
            f = pow(2, a) * pow(5, b)
            assert n2 % f == 0, (n2, a, b, f)
            g = n2 // f
            if f > g:
                continue

            ans += count_divs(math.gcd(f + n, g + n))

    return ans


def main():
    ans = 0
    for k in range(1, 10):
        cur = solve(k)
        print(k, cur)
        ans += cur

    print(ans)


if __name__ == "__main__":
    main()
