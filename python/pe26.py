best = (0, 0)
for d in range(2, 1000):
    num = 10
    seen = {}
    digits = []
    ans = -1
    # simulate long division
    while num != 0:
        if num in seen:
            ans = len(digits) - seen[num]
            break
        seen[num] = len(digits)
        q = num // d
        digits.append(q)
        num %= d
        num *= 10

    if (ans, d) > best:
        best = (ans, d)

print(*best)
