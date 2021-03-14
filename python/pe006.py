def sumsq(n):
    return sum(map(lambda x: x * x, range(1, n + 1)))

def sqsum(n):
    return sum(range(1, n + 1))**2

print(sqsum(100) - sumsq(100))
