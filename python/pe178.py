def main():
    dp = [[0 for _ in range(10)] for _ in range(1 << 10)]
    for d in range(1, 10):
        dp[1 << d][d] = 1

    ans = 0
    for l in range(2, 40 + 1):
        nxt = [[0 for _ in range(10)] for _ in dp]
        for mask, freq_table in enumerate(dp):
            for d, freq in enumerate(freq_table):
                for x in [d - 1, d + 1]:
                    if not (0 <= x < 10):
                        continue

                    nxt[mask | (1 << x)][x] += freq

        dp = nxt
        ans += sum(dp[-1])

    print(ans)

if __name__ == "__main__":
    main()
