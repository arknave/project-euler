from collections import defaultdict


def solve(w, h):
    ans = 0
    for sw in range(1, w + 1):
        for sh in range(1, h + 1):
            reps = (w + 1 - sw) * (h + 1 - sh)
            ans += reps

    for x in range(2 * w + 1):
        for y in range(2 * h + 1):
            if x % 2 != y % 2:
                continue
            for up in range(1, y + 1):
                for down in range(1, 2 * h + 1 - y):
                    assert not (y - up < 0 or y + down > 2 * h)
                    if x + up + down > 2 * w:
                        break
                    ans += 1

    return ans


def main():
    ans = 0
    for w in range(1, 47 + 1):
        for h in range(1, 43 + 1):
            ans += solve(w, h)

    print(ans)


if __name__ == "__main__":
    main()
