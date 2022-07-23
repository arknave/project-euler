from collections import defaultdict


def solve(n):
    if n % 2 == 1:
        return 0

    # state: 3 bits for the past n cells
    # bit 0 - is that cell filled?
    # bit 1 - did the ant in that cell go right?
    # bit 2 - did the ant in that cell go down?
    FILL = 0x1
    RIGHT = 0x2
    DOWN = 0x4

    dp = defaultdict(int)
    dp[0] = 1

    WORD = FILL | RIGHT | DOWN
    ALL_BITS = (1 << (3 * n)) - 1

    for r in range(n):
        for c in range(n):
            # print(r, c, len(dp))
            ndp = defaultdict(int)

            for state, freq in dp.items():
                before = state & WORD
                up = state >> (3 * (n - 1)) & WORD
                upright = state >> (3 * (n - 2)) & WORD
                entered = ((before & RIGHT) > 0) or ((up & DOWN) > 0)

                new_state = ((state << 3) | (FILL if entered else 0)) & ALL_BITS

                # if the above cell has not been entered, then we have to enter it
                # otherwise, we cannot go up.
                if r > 0 and (up & FILL) == 0:
                    if (up & DOWN) == 0:
                        # print("can go up")
                        ndp[new_state] += freq

                    continue

                # try going left
                if c > 0 and (before & FILL) == 0 and (before & RIGHT) == 0:
                    ndp[new_state | (FILL << 3)] += freq

                    if (before & DOWN) > 0:
                        # if the previous ant moves down and the cell is not filled, we have to go left
                        continue

                # can almost always go down
                if r + 1 < n:
                    ndp[new_state | DOWN] += freq

                # try going right
                if c + 1 < n and (r == 0 or (upright & DOWN) == 0):
                    ndp[new_state | RIGHT] += freq

            dp = ndp

    return sum(v for v in dp.values())


def main():
    ans = solve(10)
    print(ans)


if __name__ == "__main__":
    main()
