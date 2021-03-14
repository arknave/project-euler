CAP = 2000000
sieve = [0] * CAP 
cur = 3
ans = 2
while cur < CAP:
    if sieve[cur] == 0:
        ans += cur
        sieve[cur] = 1
        for i in range(cur, CAP, cur):
            sieve[i] = 1
    cur += 2

print(ans)
