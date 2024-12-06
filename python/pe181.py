from functools import cache
import sys

sys.setrecursionlimit(int(1e6))

def solve(b, w):
    groups = [(x, y) for x in range(b + 1) for y in range(w + 1)]

    @cache
    def inner(x, y, g):
        if x == 0 and y == 0:
            return 1
        if g == len(groups):
            return 0

        ans = 0
        k = 0
        a, b = groups[g]
        while True:
            if k * a > x or k * b > y:
                break
            ans += inner(x - k * a, y - k * b, g + 1)
            k += 1

        return ans

    return inner(b, w, 1)


def main():
    print(solve(3, 1))
    print(solve(60, 40))


if __name__ == "__main__":
    main()
