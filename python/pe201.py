def main():
    vals = [x * x for x in range(1, 101)]
    s = sum(vals)
    k = 50
    dp = [[0 for _ in range(s + 1)] for _ in range(k + 1)]
    dp[0][0] = 1
    last = 0
    for x in vals:
        for kk in range(k - 1, -1, -1):
            for y in range(min(last, s - x), -1, -1):
                dp[kk + 1][y + x] += dp[kk][y]
            last += x

    ans = sum(i for i, freq in enumerate(dp[k]) if freq == 1)

    print(ans)

if __name__ == "__main__":
    main()
