def s(n):
    res = 2
    cur = 2
    while cur % n != 0:
        res += 1
        cur *= res

    return res

def score(n, v):
    """Find largest k such that v^k divides n!"""
    ans = 0
    x = v
    while x <= n:
        ans += n // x
        x *= v

    return ans

"""x = p1^e1 p2^e2 ...
each (pi, ei) pair has some minimum y where pi^ei divides y!
take the max over all such y
there also aren't many pairs. (p, 1) = p, and ei cannot exceed... 30?
if ei == 2, p cannot exceed 10^4? precompute all up front, factorize, boom?
"""
CAP = 100000000

def gen_sieve():
    sieve = list(range(CAP + 1))
    ss = [1 for x in sieve]
    for d in range(2, CAP + 1):
        if sieve[d] == d:
            for j in range(d * d, CAP + 1, d):
                sieve[j] = d
            v = d
            p = 1
            f_val = d
            occ = 1
            while v <= CAP:
                for j in range(v, CAP + 1, v):
                    ss[j] = max(f_val, ss[j])
                v *= d
                p += 1
                while occ < p:
                    f_val += d
                    occ = score(f_val, d)
    return ss

def main():
    res = gen_sieve()
    ans = 0
    for x in range(2, CAP + 1):
        ans += res[x]

    print(ans)

main()
