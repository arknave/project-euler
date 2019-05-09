# x is outer, y is inner
# x and y need same parity
# use x^2 - y^2 tiles

# difference between two squares is 2n - 1
tiles = 1000000
ans = 0
for x in range(3, tiles + 1):
    if x * x <= tiles:
        # can use any y
        ans += (x - 1) // 2
        continue

    lo = x % 2
    hi = x
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if x * x - mid * mid <= tiles:
            hi = mid
        else:
            lo = mid
    if hi % 2 != x % 2:
        hi += 1

    gap = (x - hi) // 2
    ans += gap

print(ans)
