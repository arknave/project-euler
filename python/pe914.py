import math

"""
n^2 - m^2, 2nm, n^2 + m^2

inradius of right triangle is
.5 * (a + b - c)

Expanding by the above, inradius is 

.5 * (n^2 - m^2 + 2nm - n^2 - m^2)
.5 * (- m^2 + 2nm - m^2)
nm - m^2

want to maximize the above given n^2 + m^2 < 2r

max m (n - m)
subj to n^2 + m^2 < 2r, gcd(n, m) = 1
"""

def f(r):
    d = 2 * r
    s = math.isqrt(d)
    ans = 0
    iters = 0
    # this feels arbitrary
    for n in range(s * 925 // 1000, 1, -1):
        assert n * n < d
        start = math.isqrt(d - n * n)
        while start > 0 and (start % 2 == n % 2 or n * n + start * start >= d):
            start -= 1
        for m in range(start, 0, -2):
            assert n * n + m * m < d
            assert n % 2 != m % 2
            cur = m * (n - m)
            if cur <= ans:
                break

            if math.gcd(n, m) == 1:
                ans = cur
                print(n, m, ans)

    return ans


def main():
    print(f(10**18))

if __name__ == "__main__":
    main()
