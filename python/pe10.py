sieve = [0]*2000000
cur = 3
ans = 2
while cur < 2000000:
    if sieve[cur] == 0:
        ans += cur
        sieve[cur] = 1
        for i in xrange(cur, 2000000, cur):
            sieve[i] = 1
    cur += 2
print ans
