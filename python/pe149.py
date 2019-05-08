def row_solve(grid):
    ans = 0
    for row in grid:
        cur = 0
        for val in row:
            cur = max(0, val + cur)
            ans = max(ans, cur)

    return ans

def diag_solve(grid):
    n = len(grid)
    ans = 0
    starts = [(i, 0) for i in range(n)] + [(0, i) for i in range(1, n)]
    for x, y in starts:
        cur = 0
        for d in range(n + 1):
            if x + d >= n or y + d >= n:
                break
            cur = max(0, cur + grid[x + d][y + d])
            ans = max(ans, cur)

    return ans

def solve(grid):
    n = len(grid)
    ans = max(row_solve(grid), diag_solve(grid))
    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    ans = max(ans, row_solve(grid))
    grid = [list(reversed(row)) for row in grid]
    ans = max(ans, diag_solve(grid))
    return ans

N = 2000
grid = [[0 for _ in range(N)] for _ in range(N)]
MOD = 1000000
s = [0]
for k in range(1, N * N + 1):
    if k <= 55:
        v = (100003 - 200003 * k + 300007 * pow(k, 3, MOD)) % MOD - 500000
    else:
        v = (s[k - 24] + s[k - 55] + 1000000) % MOD - 500000
    s.append(v)

print(10, s[10])
print(100, s[100])

for i in range(N):
    for j in range(N):
        grid[i][j] = s[N * i + j + 1]

print(solve([[-2, 5, 3, 2], [9, -6, 5, 1], [3, 2, 7, 3], [-1, 8, -4, 8]]))
print(solve(grid))
