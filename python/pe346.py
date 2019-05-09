CAP = int(1e12)
base = 2
cur = base * base + base + 1
s = set()
while cur < CAP:
    while cur < CAP:
        s.add(cur)
        cur = cur * base + 1
    base += 1
    cur = base * base + base + 1

print(1 + sum(s))
