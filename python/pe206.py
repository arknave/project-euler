pows = [1]
for _ in range(20):
    pows.append(pows[-1] * 10)

def extract(x, d):
    if d == 0:
        return x % 10
    p = pows[d]
    return (x // p) % 10

def main():
    # find the unique integer which has square of the form
    # 1_2_3_4_5_6_7_8_9_0 where _ is a missing digit

    # reconstruct from the right two digits at a time
    cands = [0]
    factor = 1
    reqs = [(0, 0)] + [(2 * x, 10 - x) for x in range(1, 10)]
    pref = 2

    digs = [1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9, -1, 0]
    b = int(''.join(str(max(9, x)) for x in digs))

    while pref <= len(reqs):
        ncands = []
        for x in range(100):
            for y in cands:
                z = factor * x + y
                zz = z * z
                # print(zz, extract(zz, 2), extract(zz, 0))
                if zz <= b and all(extract(zz, a) == b for a, b in reqs[:pref]):
                    ncands.append(z)

        ncands.sort()
        cands = []
        for x in ncands:
            if not cands or cands[-1] != x:
                cands.append(x)

        print(cands)
        factor *= 100
        pref += 1

    for x in cands:
        print(x, x * x)

main()
