def a(n):
    v = 1
    l = 1
    while v != 0:
        l += 1
        v = (10 * v + 1) % n
    return l

best = 1
for i in range(1000000, 2000000):
    if i % 2 == 0 or i % 5 == 0:
        continue
    x = a(i)
    if x > 1000000:
        print(i)
        break

"""
Based on patterns, looks like its likely to be
the case that a(i) <= i
"""
