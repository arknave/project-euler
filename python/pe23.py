def d(n):
    if n < 2:
        return 0
    count = 1
    for i in xrange(2, n/2 + 1):
        if n % i == 0:
            count += i
    return count

divisors = map(d, range(0, 28124))
abundant = [i for i, x in enumerate(divisors) if x > i]

print sum(range(28124)) - sum(set([x+y for x in abundant for y in abundant if x + y < 28124]))
