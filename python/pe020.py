# sane version
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

def digitsum(n):
    if n < 10:
        return n
    return (n%10) + digitsum(n / 10)

print digitsum(fact(100))

# one liner
print sum([int(x) for x in str(reduce(lambda x, y: x*y, range(1, 100)))])
