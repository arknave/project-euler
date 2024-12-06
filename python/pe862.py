import math

def go(ways, n, d):
    if d == 10:
        if n == 0:
            return ways * (ways - 1) // 2
        return 0

    ans = 0
    for occ in range(n + 1):
        ans += go(math.comb(n, occ) * ways, n - occ, d + 1)

    return ans

def s(k):
    ans = 0
    for n0 in range(k):
        ans += go(math.comb(k - 1, n0), k - n0, 1)

    return ans

def main():
    for k in [3, 12]:
        print(s(k))


if __name__ == "__main__":
    main()
