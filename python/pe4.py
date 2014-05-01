def is_pal(n):
    return str(n) == str(n)[::-1]

maxx = 0

for i in xrange(1001):
    for j in xrange(1001):
        if is_pal(i*j):
            maxx = max(maxx, i*j)
print maxx
