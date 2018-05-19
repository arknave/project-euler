import itertools
from functools import reduce

CAP = 12000
VAL = 12500

def gen_sieve():
    sieve = list(range(VAL + 1))
    for d in range(2, VAL + 1, 2):
        sieve[d] = 2
    for d in range(3, VAL + 1, 2):
        if sieve[d] == d:
            for j in range(d * d, VAL + 1, 2 * d):
                sieve[j] = d
    return sieve

# @lru_cache(maxsize=None)
def factor(sieve, x):
    if x == 1:
        yield (1,)
        return

    p = sieve[x]
    for opt in factor(sieve, x // p):
        n = len(opt)
        for i in range(n):
            if i > 0 and opt[i] == opt[i - 1]:
                continue
            row = opt[:i] + (opt[i] * p,) + opt[i + 1:]
            yield tuple(sorted(row))
        yield tuple(sorted(opt + (p,)))

def main():
    res = [float('inf') for _ in range(CAP + 1)]
    sieve = gen_sieve()
    for x in range(2, VAL + 1):
        print(x)
        # prime factor each number
        for factor_set in factor(sieve, x):
            # print(x, factor_set)
            s = sum(factor_set)
            if s > x:
                continue
            k = x - s + len(factor_set)
            if k <= CAP:
                res[k] = min(res[k], x)

    s = set()
    for idx in range(2, CAP + 1):
        print(idx, res[idx])
        s.add(res[idx])
    print(sum(s))

main()
