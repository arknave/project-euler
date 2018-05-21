import itertools

def valid(s):
    n = len(s)
    safe = all(sum(s[:x]) > sum(s[-(x - 1):]) for x in range(2, n))
    if safe:
        ss = set()
        for mask in range(1 << n):
            cur = 0
            for i in range(n):
                if (mask & (1 << i)) > 0:
                    cur += s[i]
            ss.add(cur)
        safe = safe and len(ss) == (1 << n)

    return safe

def main():
    # seed = [11, 17, 20, 22, 23, 24]
    seed = [20, 20 + 11, 20 + 18, 20 + 19, 20 + 20, 20 + 22, 20 + 25]
    base_sum = sum(seed)
    best_sum = float('inf')
    ans = []

    DELTA = 3

    for delta in itertools.product(range(-DELTA, DELTA + 1), repeat=len(seed)):
        cur_sum = base_sum + sum(delta)
        if cur_sum >= best_sum:
            continue

        vals = [s + d for s, d in zip(seed, delta)]
        if valid(vals):
            best_sum = cur_sum
            ans = vals

    print(''.join(str(x) for x in ans))

 
main()
