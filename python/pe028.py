cap = 1001 * 1001
ans = 1
v = 1
jump = 2
while v < cap:
    # sum the corners for each "ring"
    for _ in range(4):
        v += jump
        ans += v
    jump += 2
print(ans)
