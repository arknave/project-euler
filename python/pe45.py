def tri(n):
    return n * (n + 1) / 2

def pent(n):
    return n * (3 * n - 1) / 2

def hexn(n):
    return n * (2 * n - 1)

def main():
    # find numbers that are triangular, pentagonal, and hexagonal
    ti, pi, hi = 1, 1, 1
    tn, pn, hn = tri(ti), pent(pi), hexn(hi)
    count = 0
    while count < 3:
        if tn == pn and pn == hn:
            print ti, pi, hi
            print tn, pn, hn
            count += 1
        if tn <= pn and tn <= hn:
            ti += 1
        elif pn <= tn and pn <= hn:
            pi += 1
        else:
            hi += 1
        tn, pn, hn = tri(ti), pent(pi), hexn(hi)

if __name__ == '__main__':
    main()
