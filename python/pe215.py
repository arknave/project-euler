def main():
    W = 32
    state = [[] for _ in range(W + 1)]
    state[0].append(0)
    for l in range(W + 1):
        for d in [2, 3]:
            if l + d <= W:
                for x in state[l]:
                    state[l + d].append(x | (1 << (l + d)))

    states = state[-1]

    dp = [1 for _ in states]
    H = 10
    for _ in range(2, H + 1):
        nxt = [0 for _ in states]
        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                if (s1 & s2) == (1 << W):
                    nxt[j] += dp[i]

        dp = nxt

    print(sum(dp))

if __name__ == '__main__':
    main()
