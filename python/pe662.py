from math import sqrt
MOD = int(1e9 + 7)
BOARD = 10000
CAP = int(BOARD * sqrt(2) + 10)

fib = [1, 2]
while fib[-1] < CAP:
    fib.append(fib[-1] + fib[-2])
print(fib, len(fib))
fib = set(fib)
moves = []

for dx in range(BOARD + 1):
    for dy in range(BOARD + 1):
        if dx == 0 and dy == 0:
            continue
        s = int(sqrt(dx * dx + dy * dy) + 0.5)
        if s * s != dx * dx + dy * dy or s not in fib:
            continue
        moves.append((dx, dy))

print(moves, len(moves))

dp = [[0 for _ in range(BOARD + 1)] for _ in range(BOARD + 1)]
dp[0][0] = 1
for r in range(BOARD + 1):
    for c in range(BOARD + 1):
        if dp[r][c] == 0:
            continue
        for dx, dy in moves:
            nr, nc = r + dx, c + dy
            if nr <= BOARD and nc <= BOARD:
                dp[nr][nc] += dp[r][c]
                if dp[nr][nc] >= MOD:
                    dp[nr][nc] -= MOD

print(dp[BOARD][BOARD])
