from math import ceil, sqrt

CAP = 1000000

def replace(x, a, b):
    return int(str(x).replace(str(a), str(b)))

def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False

    return True

def main():
    for i in xrange(1, CAP, 2):
        if not is_prime(i):
            continue

        rep = i
        si = str(i)
        for x in xrange(10):
            count = 1
            sx = str(x)
            for y in xrange(x + 1, 10):
                sy = str(y)
                new = replace(i, x, y)
                if sx in si and is_prime(new):
                    count += 1
                    rep = min(rep, new)

            if count >= 7:
                print '----'
                print rep, count

if __name__ == '__main__':
    main()
