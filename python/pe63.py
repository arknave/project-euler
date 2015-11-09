def main():
    ans = 0
    for base in xrange(1, 10):
        power = 1
        val = base
        while len(str(val)) == power:
            ans += 1
            power += 1
            val *= base
    print ans

if __name__ == '__main__':
    main()
