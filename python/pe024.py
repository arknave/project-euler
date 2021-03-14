def fact(n):
    if (n <= 1): return 1
    return reduce(lambda x, y: x*y, xrange(1, n+1))

def nth(n, l):
    """return the nth permutation of l"""
    if l == []:
        return []
    ll = len(l)
    options = fact(ll)
    if n >= options:
        print "ERROR"
        return []
    #[0, 1], [2, 3], [4, 5]
    bucket_size = options / ll
    bucket = n / bucket_size
    elem = l[bucket]
    return [elem] + nth(n % bucket_size, l[:bucket] + l[(bucket+1):])

print ''.join(map(str, nth(1000000-1, range(10))))
