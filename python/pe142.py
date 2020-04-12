# x + y = a^2
# x - y = b^2
# x + z = c^2
# x - z = d^2
# y + z = e^2
# y - z = f^2

# c^2 + f^2 = a^2
# b^2 + f^2 = d^2
squares = set([x * x for x in range(1, 1000000)])
for x in range(2, 500000):
    for s in squares:
        if s >= x:
            break
        y = x - s
        if x + y in squares:
            for t in squares:
                if t >= y:
                    break
                z = y - t
                if x - z in squares and x + z in squares and y + z in squares:
                    print(x, y, z, x + y + z)
