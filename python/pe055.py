def reverse_n(n):
    rev = 0
    while n != 0:
        rev += (n % 10)
        rev *= 10
        n /= 10
    return rev / 10

def is_lyrchel(x):
    start = reverse_n(x) + x
    for i in xrange(50):
        if start == reverse_n(start):
            return False
        start = reverse_n(start) + start
    return True

def main():
    print sum([1 if is_lyrchel(x) else 0 for x in range(1, 10000)])

if __name__ == '__main__':
    main()
