def tri(n):
    return n * (n + 1) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    a = n // 3
    b = n // 5
    c = n // 15
    res = 0
    res += 3 * tri(a)
    res += 5 * tri(b)
    res -= 15 * tri(c)
    
    print(res)
