from functools import lru_cache
from math import log
# on each step, your amount goes to (1 + 2f) or goes down to (1 - f)
# What's the expected value of hitting something at the end?
# Maybe take logarithms instead

# (1 + 2f)^h * (1 - f)^(1000 - h) > 1e9

FLIPS = 1000
WIN = int(1e9)

dp = [[0.0 for _ in range(FLIPS + 1)] for _ in range(FLIPS + 1)]

dp[0][0] = 1.0
for y in range(1, FLIPS + 1):
    dp[y][y] = pow(2.0, -y)
    for x in range(y - 1, 0, -1):
        dp[y][x] = 0.5 * (dp[y - 1][x] + dp[y - 1][x - 1])
    dp[y][0] = 1.0


@lru_cache(maxsize=None)
def at_least(x, y):
    if x > y:
        return 0.0
    if x == y:
        return pow(2.0, -y)
    return 0.5 * (at_least(x, y - 1) + at_least(x - 1, y - 1))

def compute(f):
    goal = log(WIN)
    for heads in range(FLIPS + 1):
        val = heads * log(1 + 2.0 * f) + (FLIPS - heads) * log(1.0 - f)
        if val > goal:
            return dp[FLIPS][heads]

    return 0.0

lo = 0.0
hi = 1.0
for _ in range(100):
    m1 = lo + (hi - lo) / 3.0
    m2 = hi - (hi - lo) / 3.0

    if compute(m1) > compute(m2):
        hi = m2
    else:
        lo = m1

print(lo, compute(lo))

