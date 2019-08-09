# (a + 2d)^2 - (a + d)^2 - a^2
# a^2 + 4ad + 4d^2 - a^2 - 2ad - d^2 - a^2
# -a^2 + 2ad + 3d^2
# (3d - a) (a + d)

# seems parabolic

def f(a, d):
    return (3 * d - a) * (a + d)

# I have no idea why this is necessary
CAP = 2000 * 2000
#CAP = 1000 * 1000
freq = [0] * CAP
for a in range(1, CAP):
    lo = 0
    hi = CAP * CAP
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if f(a, mid) <= 0:
            lo = mid
        else:
            hi = mid

    start = hi
    if f(a, start) >= CAP:
        break

    for d in range(start, CAP * CAP):
        v = f(a, d)
        assert v > f(a, d - 1)
        if v >= CAP:
            break
        freq[v] += 1
    else:
        print('MEOW', a)

ans = 0
for i in range(1, CAP):
    if freq[i] == 10 and i < 1000000:
        # print(i)
        ans += 1

print(ans)
