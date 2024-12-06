class DSU:
    def __init__(self, n):
        self.uf = list(range(n))
        self.size = [1 for _ in self.uf]

    def find(self, u):
        if self.uf[u] == u:
            return u
        v = self.find(self.uf[u])
        self.uf[u] = v

        return v

    def merge(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False

        if self.size[u] > self.size[v]:
            u, v = v, u

        self.uf[u] = v
        self.size[v] += self.size[u]
        self.size[u] = 0

        return True

M = 1000000
s = [(100003 - 200003 * k + 300007 * k * k * k) % M for k in range(1, 56)]
s.append((s[-24] + s[-55]) % M)

PM = 524287 - 1

calls = 0
dsu = DSU(M)
edge_idx = 0
while dsu.size[dsu.find(PM)] < M // 100 * 99:
    while edge_idx >= len(s):
        s.append((s[-24] + s[-55]) % M)
        s.append((s[-24] + s[-55]) % M)

    u, v = s[edge_idx:edge_idx + 2]
    u -= 1
    v -= 1
    edge_idx += 2

    calls += u != v
    dsu.merge(u, v)

print(calls)
