import itertools

m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 6]

def valid(c1, c2):
    cc1 = [m[x] for x in c1]
    cc2 = [m[x] for x in c2]
    for i in range(1, 10):
        s1 = m[(i * i) // 10]
        s2 = m[(i * i) % 10]

        here = (s1 in cc1 and s2 in cc2) or (s1 in cc2 and s2 in cc1)
        if not here:
            return False

    return True

def main():
    sides = range(0, 10)
    ans = 0

    total = 0
    for c1 in itertools.combinations(sides, 6):
        for c2 in itertools.combinations(sides, 6):
            total += 1
            if valid(c1, c2):
                ans += 1

    # order of die doesn't matter
    ans //= 2
    print(ans)

main()
