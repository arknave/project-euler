def is_pal(n):
    return str(n) == str(n)[::-1]

maxx = 0

for i in range(1001):
    for j in range(1001):
        if is_pal(i * j):
            maxx = max(maxx, i * j)
print(maxx)
