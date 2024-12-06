from functools import lru_cache


def to_base(n: int, base: int) -> list[int]:
    res = []
    while n:
        res.append(n % base)
        n //= base

    return list(reversed(res))


def solve(digits: list[int], p: int) -> int:
    @lru_cache(None)
    def dp(idx: int, bounded: bool) -> int:
        if idx == len(digits):
            return 1

        ans = 0
        max_digit = digits[idx] + 1 if bounded else p
        for d in range(max_digit):
            ans += (d + 1) * dp(idx + 1, bounded and d == digits[idx])

        return ans

    return dp(0, True)


def main():
    for v in [7, 100, int(1e9)]:
        digits = to_base(v - 1, 7)
        print(v, solve(digits, 7))


if __name__ == "__main__":
    main()
