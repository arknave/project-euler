import itertools

LETTERS = "ABCDEFGHIJKLMNOP"

def score(p):
    n = len(p)
    moves = 0
    for v in range(n):
        if p[v] == v:
            continue

        if p[-1] != v:
            moves += 1
            i = p.index(v)
            p = p[:i] + tuple(reversed(p[i:]))

        moves += 1
        p = p[:v] + tuple(reversed(p[v:]))

        assert p[v] == v

    return moves


def main():
    n = 11
    worst = 0
    k = 0
    goal = 2011
    for perm in itertools.permutations(range(n)):
        cost = score(perm)
        if cost > worst:
            worst = cost
            k = 0

        if cost == worst:
            k += 1
            if k == goal:
                print("".join(LETTERS[p] for p in perm), cost, k)


if __name__ == "__main__":
    main()
