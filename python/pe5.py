def gcd(a, b):
    if a < b: return gcd(b, a)
    if b == 0: return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b/gcd(a,b)

print reduce(lcm, range(1, 20))
