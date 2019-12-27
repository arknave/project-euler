# f(n, 1) = n
# f(n, 2) = floor(n / 2)
# f(n, 3) = ...?

# for each k, smallest where is possible is k * (k + 1) / 2
# Then increases by 1 every k

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 0 0 1 1 2 2 3 3 4 4
# 0 0 0 0 1 1 1 2 2 2 

# iterate instead over all possible K since that only goes up to sqrt(n)

ans = 0
n = 10**16
MOD = int(1e9 + 7)
for k in range(1, n + 1):
    s = k * (k + 1) // 2
    if s > n:
        break

    # how many full blocks are there?
    # n - (s - 1) slots

    full = (n - s + 1) // k
    ans += (full * (full + 1) // 2 * k) % MOD
    rem = (n - s + 1) - k * full
    ans += ((full + 1) * rem) % MOD
    ans %= MOD

print(ans)
