def pent(n):
    return n * (3 * n - 1) / 2

def main():
    # Find a pair of pentagonal numbers where the sum and difference are pentagonal
    # and the difference is minimized
    pents = map(pent, range(1, 10000))
    pents_set = set(pents)

    for i, p in enumerate(pents):
        for j in xrange(i):
            if p - pents[j] in pents_set and p + pents[j] in pents_set:
                print p - pents[j]
                return

if __name__ == '__main__':
    main()
