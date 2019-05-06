def a(n):
    v = 1
    k = 1
    while v != 0:
        v = (10 * v + 1) % n
        k += 1
    return k

def comp(n):
    for d in range(3, n, 2):
        if d * d > n:
            return False
        if n % d == 0:
            return True

    return False

ans = []
x = 91
while len(ans) < 25:
    if x % 5 == 0:
        x += 2
        continue
    if comp(x) and (x - 1) % a(x) == 0:
        ans.append(x)
    x += 2

print(ans)
print(sum(ans))
