def main():
    ans = 0
    with open('../data_files/p105_sets.txt', 'r') as fin:
        for line in fin.readlines():
            s = [int(x) for x in line.strip().split(',')]
            s.sort()
            n = len(s)
            safe = True
            for x in range(2, n):
                # first x elements must sum to more than last (x - 1) elems
                safe = safe and sum(s[:x]) > sum(s[-(x - 1):])
            if safe:
                ss = set()
                for mask in range(1 << n):
                    cur = 0
                    for i in range(n):
                        if (mask & (1 << i)) > 0:
                            cur += s[i]
                    ss.add(cur)
                safe = safe and len(ss) == (1 << n)
            if safe:
                ans += sum(s)
    print(ans)

main()
