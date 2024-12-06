from collections import deque

def f(n):
    if n <= 2:
        return n

    dist = [None for _ in range(n)]
    dist[1] = 1
    dist[2] = 2
    q = deque([1, 2])
    while q:
        u = q.popleft()
        for d in range(3):
            x = 10 * dist[u] + d
            v = x % n
            if v == 0:
                return x

            if dist[v] is None:
                dist[v] = x
                q.append(v)

    assert False

def main():
    N = 10000
    ans = 0
    for n in range(1, N + 1):
        ans += f(n) // n

    print(ans)


if __name__ == "__main__":
    main()
