def find(uf, x):
    if uf[x] == x:
        return x
    ans = find(uf, uf[x])
    uf[x] = ans
    return ans

def merge(uf, x, y):
    xr = find(uf, x)
    yr = find(uf, y)
    if xr == yr:
        return False
    uf[xr] = yr
    return True

def main():
    adj = []
    with open('../data_files/p107_network.txt', 'r') as fin:
        for line in fin.readlines():
            row = line.strip().split(',')
            row = [float('inf') if x == '-' else int(x) for x in row]
            adj.append(row)

    n = len(adj)
    total = 0
    edges = []
    for i in range(n):
        for j in range(i):
            assert adj[i][j] == adj[j][i]
            if adj[i][j] != float('inf'):
                edges.append((adj[i][j], i, j))
                total += adj[i][j]

    uf = list(range(n))
    edges.sort()
    mst = 0
    for w, u, v in edges:
        if merge(uf, u, v):
            mst += w

    print(total - mst)

main()
