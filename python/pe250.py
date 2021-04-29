def main():
    MOD = 250
    BIGMOD = 10**16
    vals = [pow(i % MOD, i, MOD) for i in range(1, 250250 + 1)]

    dp = [0 for _ in range(MOD)]
    dp[0] = 1

    for x in vals:
        ndp = list(dp)
        for i in range(MOD):
            ndp[(i + x) % MOD] += dp[i]

        dp = [x % BIGMOD for x in ndp]

    print(dp[0] - 1)


if __name__ == "__main__":
    main()
