def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def main():
    n = 4
    n2 = n * n
    masks = 1 << n2
    dp = [[0 for _ in range(n2)] for _ in range(masks)]
    for i in range(n2):
        dp[1 << i][i] = 1

    pos = [(i, j) for i in range(n) for j in range(n)]
    blocked = set()
    for i in range(n2):
        for j in range(n2):
            if i == j:
                continue
            for k in range(n2):
                if k in (i, j):
                    continue

                v1 = sub(pos[i], pos[k])
                v2 = sub(pos[j], pos[k])

                cross = v1[0] * v2[1] - v1[1] * v2[0]
                dot = v1[0] * v2[0] + v1[1] * v2[1]

                if cross == 0 and dot < 0:
                    blocked.add((i, k, j))

    for mask in range(masks):
        for i in range(n2):
            if dp[mask][i] == 0:
                continue

            for j in range(n2):
                if i == j or mask >> j & 1 == 1:
                    continue

                is_blocked = any(mask >> k & 1 == 0 and (i, k, j) in blocked for k in range(n2))
                if not is_blocked:
                    dp[mask | (1 << j)][j] += dp[mask][i]

    ans = sum(sum(row) for row in dp) - n2
    print(ans)

if __name__ == '__main__':
    main()
