ans = 0
mod = pow(10, 10)
for i in range(1, 1001):
    ans += pow(i, i, mod)
    if ans >= mod:
        ans -= mod

print(ans)
    
