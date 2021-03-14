inp = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
parsed = map(lambda x: map(int, x.split()), inp.split('\n'))

# the parents of a node are parsed[row-1][col] and parsed[row-1][col-1] (unless those are out of bounds)
best = [map(lambda _: -1, r) for r in parsed]
best[0][0] = parsed[0][0]
for i in range(1, len(parsed)):
    best[i][0] = parsed[i][0] + best[i-1][0]
    for j in range(1, len(parsed[i])-1):
        best[i][j] = parsed[i][j] + max(best[i-1][j-1], best[i-1][j])
    best[i][-1] = parsed[i][-1] + best[i-1][-1]

print max(best[-1])
