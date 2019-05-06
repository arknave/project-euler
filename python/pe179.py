n = int(1e7)
sieve = list(range(n))
for d in range(2, n):
    if sieve[d] == d:
        for j in range(d, n, d):
            sieve[j] = d

def num_div(x):
    divs = 1
    while x != 1:
        p, e = sieve[x], 0
        while x % p == 0:
            e += 1
            x //= p
        divs *= (e + 1)
    return divs

ans = 0
for d in range(2, n - 1):
    if num_div(d) == num_div(d + 1):
        ans += 1
print(ans)
