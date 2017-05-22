def main():
    n = 80
    data = [list(map(int, input().split(','))) for _ in range(n)]
    for i in range(1, n):
        data[0][i] += data[0][i - 1]
        data[i][0] += data[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            data[i][j] += min(data[i - 1][j], data[i][j - 1])

    print(data[-1][-1])

main()
