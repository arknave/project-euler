def dpf(n):
    # count the distinct prime factors of n
    dpfs = [0 if x % 2 == 1 else 1 for x in range(n)]
    for i in xrange(3, n, 2):
        if dpfs[i] == 0:
            dpfs[i] = 1
            for j in xrange(2 * i, n, i):
                dpfs[j] += 1
    return dpfs

def main():
    # Find 4 consecutive numbers that each have 4 distinct prime factors
    dpfs = dpf(1000000)
    for i, e in enumerate(dpfs):
        if e == 4 and dpfs[i - 1] == 4 and dpfs[i - 2] == 4 and dpfs[i - 3] == 4:
            print i - 3
            break

if __name__ == '__main__':
    main()
