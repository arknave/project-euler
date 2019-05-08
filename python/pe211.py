from math import sqrt
def is_square(n):
    s = int(sqrt(n))
    for d in range(-1, 2):
        if (s + d) * (s + d) == n:
            return True
    return False

CAP = 64000000
o2 = [1 for _ in range(CAP)]
ans = 1
for d in range(2, CAP):
    d2 = d * d
    for j in range(d, CAP, d):
        o2[j] += d2

    if is_square(o2[d]):
        ans += d

print(10, o2[10])
print(ans)
