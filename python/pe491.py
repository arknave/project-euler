from collections import defaultdict

def main():
    p10 = [pow(10, k, 11) for k in range(20)]
    ways0 = [0 for _ in range(11)]
    for i in range(20):
        for j in range(i + 1, 20):
            d = (p10[i] + p10[j]) % 11
            if i != 19 and j != 19:
                ways0[d] += 1
    
    dp = {(1, 1, 0): ways0[0], (2, 0, 0): ways0[2], (0, 2, 0): ways0[-2]}
    for d in range(1, 10):
        ndp = defaultdict(int)
        for k, v in dp.items():
            if k[0] + 1 <= 10 and k[1] + 1 <= 10:
                w = (10 - k[0]) * (10 - k[1])
                ndp[(k[0] + 1, k[1] + 1, k[2])] += v * w
            if k[0] + 2 <= 10:
                w = (10 - k[0]) * (9 - k[0]) // 2
                ndp[(k[0] + 2, k[1], (k[2] + d + d) % 11)] += v * w
            if k[1] + 2 <= 10:
                w = (10 - k[1]) * (9 - k[1]) // 2
                ndp[(k[0], k[1] + 2, (k[2] + 22 - d - d) % 11)] += v * w

        dp = ndp

    print(dp[10, 10, 0])

if __name__ == "__main__":
    main()
