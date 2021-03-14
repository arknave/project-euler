from math import sqrt

def cont_frac(n):
    m = 0
    d = 1
    a0 = a = int(sqrt(n))

    seen = set()
    out = []

    while True:
        if d == 0:
            return []

        m = d * a - m
        d = (n - m * m) // d

        if d == 0:
            return []

        a = (a0 + m) // d

        if (m, d) in seen:
            break

        seen.add((m, d))
        out.append(a)

    return out

def main():
    ans = 0

    for i in range(2, 10001):
        if len(cont_frac(i)) % 2 == 1:
            ans += 1

    print(ans)

main()
