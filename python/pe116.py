from functools import lru_cache

@lru_cache(maxsize=None)
def solve(l, x):
    if l < 0:
        return 0
    if l < x:
        return 1
    return solve(l - 1, x) + solve(l - x, x)

def main():
    x = 50
    print(sum([solve(x, 2) - 1, solve(x, 3) - 1, solve(x, 4) - 1]))

main()
