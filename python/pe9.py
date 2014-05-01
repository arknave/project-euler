for a in xrange(1000):
    for b in xrange(1000-a):
        c = 1000 - a - b
        if c > 0 and a*a + b*b == c*c:
            print a*b*c
