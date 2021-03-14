import itertools

def main():
    # 6 digits
    # outer 3 contribute once each
    # inner 3 contribute twice each
    NUMS = 10
    SIZE = 5

    vals = list(range(1, NUMS + 1))
    s = sum(vals)
    best = ''

    for inner in itertools.combinations(vals, SIZE):
        if (s + sum(inner)) % SIZE != 0:
            continue

        target = (s + sum(inner)) // SIZE

        outer = [x for x in vals if x not in inner]
        outer.sort()

        # fix the first element of outer, and permute everything else.
        for rest_perm in itertools.permutations(outer[1:]):
            perm = (outer[0],) + rest_perm
            for inner_perm in itertools.permutations(inner):
                bad = False
                for i in range(SIZE):
                    v = perm[i] + inner_perm[i] + inner_perm[(i + 1) % SIZE]
                    if v != target:
                        bad = True
                        break

                if not bad:
                    out = []
                    for i in range(SIZE):
                        v = perm[i] + inner_perm[i] + inner_perm[(i + 1) % SIZE]
                        out.append(perm[i])
                        out.append(inner_perm[i])
                        out.append(inner_perm[(i + 1) % SIZE])

                    outstr = ''.join(str(x) for x in out)
                    if outstr > best:
                        best = outstr

    print(best)

main()
