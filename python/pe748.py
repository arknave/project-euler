from functools import reduce
import math

def brute1(N):
    ans = 0
    k = 13
    for x in range(1, N + 1):
        for y in range(x, N + 1):
            num = k * x * x * y * y
            den = x * x + y * y
            if num % den == 0:
                z = int(math.sqrt(num // den))
                if z <= N and z * z * den == num and reduce(math.gcd, [x, y, z]) == 1:
                    # print(x, y, z)
                    ans += x + y + z

    return ans

def brute2(N):
    k = 13
    ans = 0
    for a in range(1, N + 1):
        a2 = a * a
        if a2 >= N:
            break

        b = 1
        for c in range(1, N + 1):
            if a * c >= N:
                break

            if math.gcd(a, c) > 1:
                continue

            kc2 = k * c * c
            b2 = kc2 - a2
            if b2 <= 0:
                continue

            while b * b < b2:
                b += 1

            if b * max(a, c) > N:
                break

            if b * b == b2 and a2 + b2 == kc2 and a < b and b * max(a, c) <= N and math.gcd(a, math.gcd(b, c)) == 1:
                # print(a, b, c, a * b, a * c, b * c)
                ans += a * b + a * c + b * c
                assert a <= b and c <= b

    return ans

def solve(N):
    CAP = min(int(1.01e4), int(pow(N, .25)))
    k = 13
    ans = 0
    for p in range(0, CAP):
        if p * p >= N:
            break
        for q in range(1, CAP):
            if p * p + q * q >= N:
                break

            if math.gcd(p, q) > 1:
                continue
            a = abs(2 * (p * p - 3 * p * q - q * q))
            b = abs(3 * p * p + 4 * p * q - 3 * q * q)
            c = p * p + q * q
            if max(a * b, b * c, a * c) <= N and math.gcd(a, math.gcd(b, c)) == 1:
                assert a * a + b * b == k * c * c
                # print(p, q, a, b, c)
                ans += a * b + a * c + b * c

    return ans

def main():
    # x^-2 + y^-2 = k z^-2
    # y^2 z^2 + x^2 z^2 = k x^2 y^2

    # Let a = gcd(x, y), b = gcd(x, z), c = gcd(y, z)
    # When k = 1, we have x = ab, y = ac, z = bc
    # However, here k = 13 so that may not be the case

    # Proof (k = 1):
    # Let x = a b d where p is a prime that divides d
    # We know x | yz
    # so abd | yz
    # so d | yz/(ab)
    # that means p divides y/a or z/b. This part is tricky to see, but must be true because gcd(a, z) = 1 and gcd(b, y) = 1
    # Both of these cases lead to contradictions. If ap | x and p | (y/a), then ap | x and ap | y, contradicting the gcd.

    # Now consider k = 13
    # Nothing in the above statement changes.
    # Okay, so let x = ab, y = ac, z = bc
    # We also have gcd(a, b, c) = 1
    # Now expand
    # a^2 b^2 c^4 + a^2 b^4 c^2 = k a^4 b^2 c^2
    # divide out by a^2b^2c^2
    # c^2 + b^2 = k a^2
    # This looks really close to pythagorean triples, but not quite

    # Maybe we can adapt the standard generator?
    # For n > m with gcd = 1, not both odd,
    # n^2 - m^2, 2nm, n^2 + m^2 generates
    # (n^2 - m^2)^2 + (2nm)^2
    # n^4 - 2n^2m^2 + m^4 + 4 n^2 m^2
    # Don't see anything here

    # Okay, try this
    # you know that a^2 + b^2 = k c^2 
    # find a coefficient matrix A such that
    # [a' b' c'] = A [a b c]
    # and a'^2 + b'^2 = k c'^2

    # Maybe we can focus on the smallest two options:
    # 2 3 6, 5 90 18
    # (A11 a + A12 b + A13 c)^2 + (A21 a + A22 b + A23 c)^2 = 13 (A31 a + A32 b + A33 c)^2

    # That seems hard

    # Let's try this. We know that (2, 3) is a point on the circle x^2 + y^2 = 13
    # Now fix a rational number t = p/q, for p, q in Z, q > 0, gcd(p, q) = 1
    # Find the intersection of the line going through (2, 3) with slope q and the circle x^2 + y^2 = 13

    # 1: x^2 + y^2 = 13
    # 2: (y - 3) / (x - 2) = p / q
    # 2: q y - 3 q = p x - 2 p 
    # 2: y = (p x - 2 p + 3 q) / q
    # plug back in to 1...
    # x^2 + [(p x - 2 p + 3 q) / q]^2 = 13
    # q^2 x^2 + (p x - 2 p + 3 q)^2 = 13 q^2
    # q^2 x^2 + p^2 x^2 - 4 p^2 x + 4 p^2 + 6 p q x - 12 p q + 9 q^2 = 13 q^2
    # (p^2 + q^2) x^2 + (6 p q - 4 p^2) x = - 4 p^2 + 12 p q + 4 q^2
    # Ignore this, time for wolfram alphao
    # x = 2(p^2 - 3 p q - q^2) / (p^2 + q^2), y = -3p^2 - 4 p q + 3 q^2 / (p^2 + q^2)

    print(100, brute1(100), brute2(100), solve(100))
    print(1000, brute1(1000), brute2(1000), solve(1000))
    print(100000, brute2(100000), solve(100000))
    print(10**16, solve(10**16))

if __name__ == "__main__":
    main()
