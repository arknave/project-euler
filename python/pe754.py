MOD = int(1e9 + 7)

def main():
    n = 10**8
    pdivs = [[] for _ in range(n + 1)]
    ans = 1
    for d in range(2, n + 1):
        if not pdivs[d]:
            for j in range(d, n + 1, d):
                pdivs[j].append(d)

        k = len(pdivs[d])
        exp = 0
        for mask in range(1 << k):
            sgn = 1
            v = 1
            for i in range(k):
                if mask & (1 << i):
                    sgn = -sgn
                    v *= pdivs[d][i]

            exp += sgn * ((n // v) - (d // v))

        ans = ans * pow(d, exp, MOD) % MOD

    print(ans)

if __name__ == "__main__":
    main()
