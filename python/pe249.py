from collections import defaultdict

def gen_sieve(n):
    sieve = [False for _ in range(n + 1)]
    primes = [2]
    for d in range(3, n, 2):
        if not sieve[d]:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = True

    return sieve, primes


def main():
    MOD = 10**16

    CAP = 1550000
    n = 5000
    sieve, primes = gen_sieve(CAP)

    dp = [0] * (CAP + 1)
    dp[0] = 1

    for x in primes:
        if x > n:
            break

        for j in range(CAP - x, -1, -1):
            dp[j + x] += dp[j]

    ans = sum(v for k, v in enumerate(dp) if not sieve[k]) % MOD

    print(ans)


if __name__ == "__main__":
    main()
