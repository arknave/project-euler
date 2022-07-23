from functools import lru_cache

MOD = int(1e9 + 7)
INV4 = (MOD + 1) // 4

@lru_cache()
def solve(n, b):
    """Tuple of (Ways, orsum)"""
    if n < 0:
        return (0, 0)
    if b == 0:
        return (1, 0)

    rem = 2 * b - 1
    if 2 * rem <= n:
        ways = 1
        orsum = 0
        while b > 0:
            ways = 4 * ways % MOD
            orsum += 3 * b % MOD
            
            b >>= 1

        orsum = orsum * ways % MOD * INV4 % MOD

        return (ways, orsum)

    res = [0, 0]
    for x in range(2):
        for y in range(2):
            s = (x + y) * b
            contrib = b if x | y > 0 else 0
            ways, orsum = solve(n - s, b // 2)
            res[0] += ways
            res[1] += orsum + ways * contrib

            res[0] %= MOD
            res[1] %= MOD

    return tuple(res)

def G(n):
    res = 0
    for k in range(n + 1):
        for i in range(k + 1):
            res += i | (k - i)

    return 2 * res

def main():
    print(10, G(10), solve(10, 16)[1] * 2)
    print(100, G(100), solve(100, 128)[1] * 2)
    print(10**18, solve(10**18, 1 << 61)[1] * 2 % MOD)

if __name__ == "__main__":
    main()
