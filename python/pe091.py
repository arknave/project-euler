import itertools

def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def mag(v):
    return v[0] * v[0] + v[1] * v[1]

def is_right(v1, v2):
    d1 = cross(v1, v2)
    d2 = mag(v1) * mag(v2)

    return d1 * d1 == d2

def main():
    n = 50
    valid = set()
    for x1, y1, x2, y2 in itertools.product(range(n + 1), repeat=4):
        v1 = (x1, y1)
        v2 = (x2, y2)
        v3 = (x1 - x2, y1 - y2)

        v = [v1, v2, v3]

        if (0, 0) in v or v1 > v2:
            continue

        if any(is_right(a, b) for a, b in itertools.combinations(v, 2)):
            valid.add((v1, v2))

    print(len(valid))

main()
