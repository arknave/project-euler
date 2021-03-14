def d(n):
    if n < 2:
        return 0
    count = 1
    for i in xrange(2, n/2 + 1):
        if n % i == 0:
            count += i
    return count

summ = 0
divisors = map(d, range(0, 10001))
for i, d in enumerate(divisors):
    if d < 10001 and divisors[d] == i and divisors[d] != d:
        summ += i

print summ
