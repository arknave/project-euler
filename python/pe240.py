import functools
import math

@functools.cache
def solve(n, k, tot, dig):
    """
    How many ways are there to roll n die such that the top k sum to tot?
    """
    assert n >= k
    if n == 0:
        return 1 if tot == 0 else 0
    if dig == 0:
        return 0

    ans = 0
    for land in range(n + 1):
        contrib = min(land, k) * dig
        if contrib > tot:
            break

        ans += math.comb(n, land) * solve(n - land, max(0, k - land), tot - contrib, dig - 1)

    return ans

def main():
    print(solve(5, 3, 15, 6))
    print(solve(20, 10, 70, 12))

if __name__ == "__main__":
    main()
