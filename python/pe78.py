MOD = 1000000

# Magic Pentagonal numbers
def g(k):
    return k * (3 * k - 1) // 2

def main():
    p = [1]
    n = 1
    # skip 0
    gs = [(g(k), k & 1) for k in range(1, 1000)]
    gs += [(g(k), k & 1) for k in range(-1000, 0)]
    gs.sort()
    while p[-1] % MOD != 0:
        v = 0
        for x, s in gs:
            if x > n:
                break
            if s == 0:
                v -= p[n - x]
            else:
                v += p[n - x]

        p.append(v % MOD)
        n += 1

    print(len(p) - 1)

main()
