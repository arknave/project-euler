from math import ceil, sqrt
def count_divisors(n):
    count = 2
    for i in xrange(2, int(ceil(sqrt(n)))):
        if n%i == 0:
            count += 1 if i*i == n else 2
    return count

def tri(n):
    return cur_n*(cur_n+1) >> 1

cur_n = 1
while count_divisors(tri(cur_n)) < 500:
    cur_n += 1

print tri(cur_n)
