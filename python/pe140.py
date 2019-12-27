from math import gcd, sqrt

# A_G(x) = 1x + 4x^2 + 5x^3 + 9x^4 + 14x^5 + 23x^6 + ...
# A_G(x) = 1x + 3x^2 + ...
#        = 0x + 1x^2 + 4x^3 + 5x^4 +  9x^5 + 14x^6 + ...
#                    + 1x^3 + 4x^4 +  5x^5 +  9x^6 + ...

# A_G(x) = 1x + 3x^2 + xA_G(x) + x^2A_G(x)
# y = x + 3x^2 + xy + x^2 y
# q^2 y = p q + 3p^2 + p q y + p^2 y
# 0 = p q + 3p^2 + p q y + p^2 y - q^2 y
# 0 = p q + 3p^2 + (p q + p^2 - q^2) y
# -(pq + 3p^2) /(p q + p^2 - q^2) = y

g = [1, 4]

nugs = []

TARGET = (1.0 + sqrt(5.0)) / 2.0 - 1.0

bounds = [(200, TARGET), (int(1e4), 1e-2), (int(1e5), 1e-4), (int(1e6), 1e-6), (float('inf'), 1e-8)]

for q in range(1, int(1e7)):
    for cap, delta in bounds:
        if q < cap:
            lo = TARGET - delta
            hi = TARGET + delta
            break

    plo = int(q * lo)
    phi = int(q * hi) + 1

    for p in range(plo, phi):
        if gcd(p, q) != 1:
            continue

        num = p * q + 3 * p * p
        den = -(p * q + p * p - q * q)
        # print(p, q, num, den)
        if num > 0 and den > 0 and num % den == 0:
            print(p, q, p / q, num // den)
            nugs.append(num // den)

    q += 1

nugs.sort()
print('Found', len(nugs))
print(sum(nugs[:30]))
