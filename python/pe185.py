import itertools
import math


def solve(clues, valid, idx):
    if any(x == 0 for x in valid):
        return None
    if idx == len(clues):
        return [math.log2(x) for x in valid]

    n = len(valid)
    key, k = clues[idx]
    # assert len(key) == n, valid

    possible = []
    for i in range(n):
        if (valid[i] & (1 << key[i])) > 0:
            possible.append(i)

    for sub in itertools.combinations(possible, k):
        new_valid = []
        for i in range(n):
            if i in sub:
                new_valid.append(1 << key[i])
            else:
                new_valid.append(valid[i] & ~(1 << key[i]))

        res = solve(clues, new_valid, idx + 1)
        if res is not None:
            return res

    return None


def main():
    clues = [
        (tuple(map(int, s)), k)
        for s, k in [
            ("70794", 0),
            ("34109", 1),
            ("12531", 1),
            ("90342", 2),
            ("39458", 2),
            ("51545", 2),
        ]
    ]
    n = 5

    clues = [
        (tuple(map(int, s)), k)
        for s, k in [
            ("5616185650518293", 2),
            ("3847439647293047", 1),
            ("5855462940810587", 3),
            ("9742855507068353", 3),
            ("4296849643607543", 3),
            ("3174248439465858", 1),
            ("4513559094146117", 2),
            ("7890971548908067", 3),
            ("8157356344118483", 1),
            ("2615250744386899", 2),
            ("8690095851526254", 3),
            ("6375711915077050", 1),
            ("6913859173121360", 1),
            ("6442889055042768", 2),
            ("2321386104303845", 0),
            ("2326509471271448", 2),
            ("5251583379644322", 2),
            ("1748270476758276", 3),
            ("4895722652190306", 1),
            ("3041631117224635", 3),
            ("1841236454324589", 3),
            ("2659862637316867", 2),
        ]
    ]
    n = 16
    clues.sort(key=lambda x: x[1])

    valid = [(1 << 10) - 1 for _ in range(n)]

    ans = solve(clues, valid, 0)
    print(ans)
    print("".join(str(int(x)) for x in ans))


if __name__ == "__main__":
    main()
