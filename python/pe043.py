import itertools

def main():
    primes = [2, 3, 5, 7, 11, 13, 17]
    ans = 0
    for perm in itertools.permutations(range(10)):
        works = True
        for i, p in zip(range(1, 8), primes):
            v = 100 * perm[i] + 10 * perm[i + 1] + perm[i + 2]
            if v % p != 0:
                works = False
                break
        if works:
            ans += int(''.join(str(x) for x in perm))

    print(ans)

if __name__ == '__main__':
    main()
