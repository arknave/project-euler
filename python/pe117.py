from functools import lru_cache

@lru_cache(maxsize=None)
def solve(l):
    if l < 0:
        return 0
    if l == 0:
        return 1
    return sum(solve(l - x) for x in range(1, 5))

def main():
    x = 50
    print(solve(5))
    print(solve(50))

main()
