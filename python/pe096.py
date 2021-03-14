# TODO: This is embarassingly slow
from collections import Counter
from functools import reduce

def valid_box(sudoku, a, b):
    c = Counter()
    for i in range(3 * a, 3 * a + 3):
        for j in range(3 * b, 3 * b + 3):
            c[sudoku[i][j]] += 1

    return all(c[x] <= 1 or x == 0 for x in c)

def valid(sudoku):
    def _valid(row):
        c = Counter(row)
        return all(c[x] <= 1 or x == 0 for x in c)

    return all(_valid(row) for row in sudoku) \
       and all(_valid(col) for col in zip(*sudoku)) \
       and all(valid_box(sudoku, i, j) for i in range(3) for j in range(3))

def solve(sudoku):
    if not valid(sudoku):
        return None

    if all(all(x != 0 for x in row) for row in sudoku):
        return 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                x, y = i, j

    for k in range(1, 10):
        sudoku[x][y] = k
        s = solve(sudoku)
        if s is not None:
            return s

    sudoku[x][y] = 0

    return None

def main():
    n = 50
    fin = open('../data_files/p096_sudoku.txt')
    ans = 0
    for x in range(n):
        print(x)
        fin.readline()
        sudoku = [list(map(int, fin.readline().strip())) for _ in range(9)]
        ans += solve(sudoku)

    fin.close()

    print(ans)

main()
