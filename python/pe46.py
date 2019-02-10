CAP = 10000

def gen_primes(tot):
    sieve = [True for _ in range(tot + 1)]
    primes = [2]
    for d in range(3, tot + 1, 2):
        if sieve[d]:
            primes.append(d)
            for j in range(d * d, tot + 1, 2 * d):
                sieve[j] = False

    return primes

primes = set(gen_primes(CAP))
twice_squares = set(2 * x * x for x in range(CAP))

def goldbach(x):
    if x in primes:
        return True
    for p in primes:
        if p < x and x - p in twice_squares:
            return True

    return False

def main():
    ans = 3
    while goldbach(ans):
        ans += 2

    print(ans)

if __name__ == '__main__':
    main()
