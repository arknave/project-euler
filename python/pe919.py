# per https://proofwiki.org/wiki/Distance_from_Vertex_of_Triangle_to_Orthocenter
# CH = 2R cos C
# Where H is orthocenter and R is circumradius
# Thus, cosC = 1/4
# a^2 + b^2 - 2ab cosC = c^2
# a^2 + b^2 +- ab/2 = c^2
# 2a^2 + 2b^2 +- ab = 2c^2

from fractions import Fraction as Q
import math

def brute(n):
    ans = 0
    for a in range(1, n):
        for b in range(a, n):
            if a % 2 == 1 and b % 2 == 1:
                continue

            # At least one of a or b must be even
            for sgn in [-1, 1]:
                c2 = 2 * a * a + 2 * b * b + sgn * a * b
                assert c2 % 2 == 0
                c2 //= 2
                c = math.isqrt(c2)
                p = a + b + c
                if p <= n and c * c == c2:
                    ans += a + b + c
    return ans

# 2a^2 + 2b^2 + ab = 2c^2
# Let x = a/c, y = b/c
# 2x^2 + 2y^2 + xy = 2
# Base solutions are (+-1, 0) and (0, +-1)

# Fix a line with slope (tmx, tmy) that goes through (-1, 0)
# Then we have
# x' = tmx - 1
# y' = tmy
# 2(tmx - 1)^2 + 2(tmy)^2 + ((tmx - 1) tmy) = 2

n = int(1e7)
B = 6500

seen = set()
for mx in range(B):
    for my in range(1, mx):
        if mx == 0 and my == 0 or math.gcd(mx, my) != 1:
            continue
        t = Q(4 * mx + my, 2 * mx * mx + 2 * my * my + mx * my)
        x = t * mx - 1
        y = t * my
        c = max(x.denominator, y.denominator)
        a = int(x * c)
        b = int(y * c)
        if a <= 0 or b <= 0 or c <= 0:
            continue
        assert math.gcd(a, b, c) == 1
        sides = tuple(sorted([a, b, c]))
        if sides[0] + sides[1] <= sides[2]:
            continue
        seen.add(sides)
for mx in range(B):
    for my in range(1, mx):
        if mx == 0 and my == 0 or math.gcd(mx, my) != 1:
            continue
        t = Q(4 * mx - my, 2 * mx * mx + 2 * my * my - mx * my)
        x = t * mx - 1
        y = t * my
        assert 2 * x * x + 2 * y * y - x * y == 2
        c = max(x.denominator, y.denominator)
        a = int(x * c)
        b = int(y * c)
        if a <= 0 or b <= 0 or c <= 0:
            continue
        assert math.gcd(a, b, c) == 1
        sides = tuple(sorted([a, b, c]))
        if sides[0] + sides[1] <= sides[2]:
            continue
        seen.add(sides)

ans = 0
for t in seen:
    p = sum(t)
    k = n // p
    ans += p * k * (k + 1) // 2

print(ans)
