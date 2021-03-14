from functools import reduce

def inc(rolls, sides):
    n = len(rolls)
    new_rolls = [0.0 for _ in range(n + sides)]
    for i, x in enumerate(rolls):
        for j in range(1, sides + 1):
            new_rolls[i + j] += x / sides

    return new_rolls

def var(s):
    mean = sum(i * p for i, p in enumerate(s))
    ans = 0.0
    for i, p in enumerate(s):
        ans += p * (i - mean) ** 2

    return ans

def main():
    dice = [4, 6, 8, 12, 20]

    # dp[i] = probability of ending at sum i
    dp = [0.0, 1.0]

    n = 1
    EPS = 1e-9
    for sides in dice:
        n *= sides
        ndp = [0.0 for _ in range(n + 1)]
        rolls = [1.0]

        for i, p in enumerate(dp):
            if i == 0:
                continue

            rolls = inc(rolls, sides)

            for j, q in enumerate(rolls):
                ndp[j] += p * q

        # dp = [x if x > EPS else 0.0 for x in ndp]
        dp = ndp

        print(dp, sum(dp), sides, n, var(dp))

        # what is variance?
        # variance = E[(x - mean)^2]

if __name__ == "__main__":
    main()
