from collections import deque

def main():
    with open('../data_files/p079_keylog.txt') as fin:
        codes = [line.strip() for line in fin.readlines()]

    used = set(int(c) for word in codes for c in word)
    graph = [[] for _ in range(10)]
    in_deg = [0 for _ in range(10)]
    for code in codes:
        for i in range(2):
            a = int(code[i])
            b = int(code[i + 1])
            graph[a].append(b)
            in_deg[b] += 1

    dq = deque()
    for x in range(10):
        if x in used and in_deg[x] == 0:
            dq.append(x)

    res = []
    while dq:
        x = dq.popleft()
        res.append(str(x))
        for v in graph[x]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                dq.append(v)

    print(''.join(res))

main()
