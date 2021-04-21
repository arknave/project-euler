def main():
    n = 32
    comb = [[1]]
    for i in range(1, n + 1):
        row = [1]*(i + 1)
        for j in range(1, i):
            row[j] = comb[-1][j - 1] + comb[-1][j]

        comb.append(row)

    # E[n] = exp number of rounds to get n bits set
    # E[n] = sum_{k = 0}^n (nCk / 2^N) (E[k] + 1)
    # Remote the k=n term from RHS to get...
    E = [0]
    p2 = 1.0
    for i in range(1, n + 1):
        p2 *= 2;
        ans = 1.0
        for j in range(i):
            ans += comb[i][j] * E[j] / p2

        ans *= p2
        ans /= (p2 - 1.0)

        E.append(ans)

    print(E[32])

main()
