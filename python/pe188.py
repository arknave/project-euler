def phi(x):
    res = 1
    e2 = 0
    while x % 2 == 0:
        e2 += 1
        x //= 2

    if e2 > 0:
        res *= (1 << e2) - (1 << (e2 - 1))

    for d in range(3, x, 2):
        if d * d > x:
            break
        v = 1
        while x % d == 0:
            x /= d
            v *= d
        if v > 1:
            res *= v - (v // d)

    return res

def hyp_exp(a, b, m):
    if m == 1:
        return 0
    if b == 1:
        return a % m
    e = hyp_exp(a, b - 1, phi(m))
    return pow(a, e, m)

print(3, 2, hyp_exp(3, 2, int(1e8)))
print(3, 3, hyp_exp(3, 3, int(1e8)))
print(3, 4, hyp_exp(3, 4, int(1e8)))
print(1777, 1855, hyp_exp(1777, 1855, int(1e8)))
