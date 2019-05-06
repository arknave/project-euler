from math import gcd

def abc(rad, c):
    if rad[c] == c:
        return 0

    x = 0
    for a in range(1, c):
        if a + a > c:
            break
        b = c - a
        if gcd(a, b) != 1:
            continue
        if rad[a] * rad[b] * rad[c] < c:
            x += 1

    return x

def main():
    CAP = 120000
    rad = [1 for _ in range(CAP)]
    for d in range(2, CAP):
        if rad[d] == 1:
            for x in range(d, CAP, d):
                rad[x] *= d
    tot = 0
    ans = 0
    for c in range(1, CAP):
        v = abc(rad, c)
        tot += v
        ans += c * v
    print(tot, ans)

main()
