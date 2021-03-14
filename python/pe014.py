cap = 1000000
memo = [-1]*cap
memo[1] = 1

ans = 1
best = 1
for n in xrange(1,cap):
    count = 1
    i = n
    while i != 1:
        count += 1
        i = 3*i + 1 if i % 2 == 1 else i / 2
        if i < cap and memo[i] > -1:
            count += memo[i]
            i = 1
    memo[n] = count
    if count > best:
        best = count
        ans = n

print ans, best
