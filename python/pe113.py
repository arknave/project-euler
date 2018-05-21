def inc(max_len):
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ans = sum(dp)
    for l in range(2, max_len):
        new = [sum(dp[:i + 1]) for i in range(10)]
        dp = new
        ans += sum(new)
    return ans

def dec(max_len):
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ans = sum(dp)
    for l in range(2, max_len):
        new = [sum(dp[i:]) for i in range(10)]
        dp = new
        ans += sum(new)
    return ans

def solve(exp):
    return inc(exp + 1) + dec(exp + 1) - 9 * exp

def main():
    print(solve(6))
    print(solve(10))
    print(solve(100))

main()
