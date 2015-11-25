from math import sqrt, ceil

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in xrange(3, int(ceil(sqrt(x))) + 1, 2):
        if x % i == 0:
            return False

    return True

def main():
    c = 1
    diag_dist = 0
    prime_count = 0
    size = 1

    while prime_count < 5 or 1.0 * prime_count / (2.0 * size - 1.0) > 0.1:
        diag_dist += 2

        for _ in xrange(4):
            c += diag_dist
            if is_prime(c):
                prime_count += 1

        size += 2

        print prime_count, size
    print size

if __name__ == '__main__':
    main()
