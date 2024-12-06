from functools import cache

def solve(w, h):
    # down, left, right, mask
    pieces = [
        (2, 1, 2, (1 | 2 | (1 << w))),
        (2, 1, 2, (1 | 2 | (1 << (w + 1)))),
        (2, 1, 2, (1 | (1 << w) | (1 << (w + 1)))),
        (2, 2, 1, (1 | (1 << (w - 1)) | (1 << w))),
        (3, 1, 1, (1 | (1 << w) | (1 << (w + w)))),
        (1, 1, 3, (1 | 2 | 4)),
    ]

    n = w * h
    @cache
    def inner(idx, mask):
        if idx == n:
            assert mask == 0
            return 1
        if (mask & 1) == 1:
            return inner(idx + 1, mask >> 1)

        r, c = idx // w, idx % w
        ans = 0
        for i, (down, left, right, piece_mask) in enumerate(pieces):
            valid = r + down <= h and c + right <= w and c + 1 >= left and (mask & piece_mask) == 0
            if valid:
                ans += inner(idx + 1, (mask | piece_mask) >> 1)

        return ans

    return inner(0, 0)

def main():
    print(solve(2, 9))
    print(solve(9, 12))


if __name__ == "__main__":
    main()
