from collections import deque

def triangle(n):
    return n * (n + 1) // 2

def square(n):
    return n * n

def pentagonal(n):
    return n * (3 * n - 1) // 2

def hexagonal(n):
    return n * (2 * n - 1)

def heptagonal(n):
    return n * (5 * n - 3) // 2

def octogonal(n):
    return n * (3 * n - 2)

def get_values(f):
    return [f(x) for x in range(2000) if 1000 <= f(x) < 10000]

def get_bigrams(row):
    out = set()
    for value in row:
        out.add(value % 100)
        out.add(value // 100)

    return out

def dfs(values, x, y, state):
    if x >= len(values) or len(state) >= len(values):
        if state[-1][-1] % 100 == state[0][1] // 100:
            print(state, sum(y for _, y in state))
        return

    if len(state) == 0 or (state[-1][-1] % 100) == (values[x][y] // 100):
        new_state = deque(state)
        new_state.append((x, values[x][y]))
        taken_rows = set(x for x, _ in new_state)
        for row in range(len(values)):
            if row not in taken_rows:
                dfs(values, row, 0, new_state)

        if len(new_state) == len(values):
            dfs(values, len(values), len(values), new_state)

    if y + 1 < len(values[x]):
        dfs(values, x, y + 1, state)

def main():
    functions = [triangle, square, pentagonal, hexagonal, heptagonal, octogonal]
    values = list(map(get_values, functions))

    dfs(values, 0, 0, deque())

main()
