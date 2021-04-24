MOD = int(1e9 + 7)

def s(n):
    n9 = n // 9
    rem = n % 9

    return ((rem + 1) * pow(10, n9, MOD) % MOD - 1) % MOD

def S_brute(n):
    ans = 0
    for i in range(1, n + 1):
        ans += s(i)
        ans %= MOD

    return ans

def S_fast(n):
    ans = 0
    while n % 9 > 0:
        ans += s(n)
        ans %= MOD
        n -= 1

    k = n // 9
    # 45 * 11111... = 5 * (10^k - 1)
    ans += (5 * (pow(10, k, MOD) - 1)) % MOD

    # 9 * 1 + 9 * 11 + 9 * 111 + ...
    # 9 \sum_{i=1}^{k-1} (10^i - 1)
    # 9 [[\sum_{i=1}^{k-1} 10^i] - k]
    # (10^k - 1) - 9k
    ans += pow(10, k, MOD) - 9 * k - 1
    ans %= MOD

    return ans


def main():
    print("s(10)", s(10))
    print("S(20)", S_brute(20), S_fast(20))

    a, b = 0, 1
    ans = 0
    for i in range(2, 91):
        a, b = b, a + b
        ans += S_fast(b)
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()
