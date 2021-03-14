import heapq
def main():
    n = 80
    data = [list(map(int, input().split(','))) for _ in range(n)]
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    pq = []
    dist[0][0] = data[0][0]
    heapq.heappush(pq, (data[0][0], 0, 0))

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Why use DP when you have Dijkstra? :D
    while pq:
        d, x, y = heapq.heappop(pq)
        if dist[x][y] < d:
            continue

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                ndist = d + data[nx][ny]
                if ndist < dist[nx][ny]:
                    dist[nx][ny] = ndist
                    heapq.heappush(pq, (ndist, nx, ny))

    print(dist[-1][-1])

main()
