with open("../data_files/pe067_triangle.txt", "r") as fin:
    inp = fin.readlines()
    parsed = [[int(x) for x in row.strip().split()] for row in inp]

# the parents of a node are parsed[row-1][col] and parsed[row-1][col-1] (unless those are out of bounds)
best = [[-1 for _ in r] for r in parsed]
best[0][0] = parsed[0][0]
for i in range(1, len(parsed)):
    best[i][0] = parsed[i][0] + best[i - 1][0]
    for j in range(1, len(parsed[i]) - 1):
        best[i][j] = parsed[i][j] + max(best[i - 1][j - 1], best[i - 1][j])
    best[i][-1] = parsed[i][-1] + best[i - 1][-1]

print(max(best[-1]))
