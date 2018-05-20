def main():
    cap = 1000000
    follow = [1 for _ in range(cap + 1)]
    for d in range(2, cap):
        for j in range(2 * d, cap + 1, d):
            follow[j] += d

    in_deg = [0 for _ in range(cap + 1)]
    for i in range(1, cap + 1):
        if follow[i] <= cap:
            in_deg[follow[i]] += 1

    srcs = []
    for i in range(1, cap + 1):
        if in_deg[i] == 0:
            srcs.append(i)

    root = [-1 for _ in range(cap + 1)]
    cycs = []
    for src in srcs:
        # print('Starting with', src)
        stk = [src]
        root[src] = src
        while stk:
            x = stk.pop()
            # print('vis', x)
            if follow[x] <= cap:
                if root[follow[x]] == -1:
                    stk.append(follow[x])
                    root[follow[x]] = src
                elif root[follow[x]] == src:
                    cycs.append(follow[x])

    ans = 1
    best_chain = []
    for cyc in cycs:
        chain = [follow[cyc]]
        while chain[-1] != cyc:
            chain.append(follow[chain[-1]])
        if len(chain) > ans:
            ans = len(chain)
            best_chain = chain
        print(cyc, chain, min(chain))
    print(ans, min(best_chain))

main()
