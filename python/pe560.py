import itertools
import math

MOD = int(1e9 + 7)


def brute_grundy(n):
    grundy = [0 for _ in range(n)]
    for i in range(1, n):
        seen = set()
        for j in range(1, i + 1):
            if math.gcd(i, j) == 1:
                seen.add(grundy[i - j])

        while grundy[i] in seen:
            grundy[i] += 1

    return grundy

def fast_grundy(n):
    grundy = [0 for _ in range(n)]
    grundy[1] = 1
    nxt = 2
    for i in range(3, n, 2):
        if grundy[i] == 0:
            grundy[i] = nxt
            for j in range(i * i, n, i + i):
                if grundy[j] == 0:
                    grundy[j] = nxt
            nxt += 1

    return grundy


def fwht(a):
    b = 1
    while b < len(a):
        for i in range(0, len(a), b + b):
            for j in range(i, i + b):
                x = a[j]
                y = a[j + b]
                a[j] = (x + y) % MOD
                a[j + b] = (x - y) % MOD
        b *= 2


def l(n, k):
    grundy = fast_grundy(n)

    p2 = 1
    while p2 < n:
        p2 *= 2

    freq = [0 for _ in range(p2)]
    for x in grundy:
        freq[x] += 1

    freq[0] -= 1

    # print("fast grundy", grundy)
    # print(freq)
    fwht(freq)
    # print(freq)
    freq = [pow(x, k, MOD) for x in freq]
    # print(freq)
    fwht(freq)
    # print(freq)
    freq = [x * pow(p2, MOD - 2, MOD) % MOD for x in freq]
    # print(freq)

    return freq[0]


def l_brute(n, k):
    grundy = brute_grundy(n)
    p2 = 1
    while p2 < n:
        p2 *= 2

    # print("slow grundy", grundy)
    dp = [0 for _ in range(p2)]
    dp[0] = 1
    for _ in range(k):
        nxt = [0 for _ in range(p2)]
        for src in range(p2):
            for s in range(1, n):
                nxt[src ^ grundy[s]] += dp[src]
        dp = nxt
        # print(dp)

    # print(dp)
    return dp[0]

def brute2(n, k):
    grundy = brute_grundy(n)
    ans = 0
    for p in itertools.product(range(1, n), repeat=k):
        cur = 0
        for x in p:
            cur ^= grundy[x]

        ans += (cur == 0)

    return ans

def main():
    for n, k in [(5, 2), (10, 5), (10, 10)]: #, (1000, 1000)]:
        # print(n, k, l(n, k), l_brute(n, k))
        ans = l(n, k)
        exp = l_brute(n, k)
        print(ans, exp)

    print(l(1000, 1000))

    n = 10**7
    print(l(n, n))


if __name__ == "__main__":
    main()
