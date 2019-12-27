from math import gcd

# A_F(x) = 1x + 1x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + ...
# A_F(x) = 0x + 1x^2 + 1x^3 + 2x^4 + 3x^5 + 5x^6 + ...
#             + 0x^2 + 1x^3 + 1x^4 + 2x^5 + 5x^6 + ...

# A_F(x) = x + x A_F(x) + x^2 A_F(x)
# y = x(1 + y + x y)
# Write x as a rational: p/q
# Then we have
# y = p/q (1 + y + p y / q), which are all integers
# y = p/q + yp / q + p^2 y / q^2
# q^2 y = q p + q yp + p^2 y
# 0 = pq + pq y + p^2 y - q^2 y
# 0 = pq + (pq + p^2 - q^2) y
# -pq / (pq + p^2 - q^2) = y

f = [1, 2]

for i in range(15):
    p, q = f[-2:]
    num = p * q
    den = -(p * q + p * p - q * q)
    assert num > 0 and den > 0 and num % den == 0
    print(i + 1, p, q, num // den)

    f.append(f[-2] + f[-1])
    f.append(f[-2] + f[-1])
