def gen_totient(n):
    totient = list(range(n + 1))
    for p in range(2, n + 1):
        if totient[p] == p:
            for j in range(p, n + 1, p):
                totient[j] //= p
                totient[j] *= p - 1

    return totient

N = int(4e7)
phi = gen_totient(N)
dist = [0 for _ in range(N + 1)]
dist[1] = 1
for x in range(2, N + 1):
    dist[x] = dist[phi[x]] + 1

ans = 0
for p in range(2, N + 1):
    if dist[p] == 25 and phi[p] + 1 == p:
        print(p)
        ans += p

print(ans)
