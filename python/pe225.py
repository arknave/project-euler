def divides(x):
    a, b, c = 1, 1, 1
    seen = set()
    while True:
        seen.add((a, b, c))
        d = (a + b + c) % x
        if d == 0:
            return True
        if (b, c, d) in seen:
            return False
        a, b, c = b, c, d
    return False

d = 3
ans = []
while len(ans) < 124:
    if not divides(d):
        ans.append(d)
    d += 2

print(ans[-1])
