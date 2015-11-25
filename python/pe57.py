from fractions import Fraction

def main():
    num = 3
    den = 2
    count = 0
    for _ in xrange(1000):
        num, den = 2 * den + num, num + den
        if len(str(num)) > len(str(den)):
            print num, den
            count += 1
    print count

if __name__ == '__main__':
    main()
