def is_prime(s, n):
    return s[n] == 1

def gen_sieve(n):
    sieve = [1 if x % 2 == 1 else 0 for x in range(n)]
    sieve[0] = 0
    sieve[1] = 0
    sieve[2] = 1
    primes = [2]
    for i in xrange(3, n, 2):
        if sieve[i] == 1:
            primes.append(i)
            for j in xrange(i * i, n, i):
                sieve[j] = 0

    return sieve, primes

def trunc(s, p):
    p_copy = p
    while p_copy > 0:
        if not is_prime(s, p_copy):
            return False
        p_copy /= 10

    pow10 = 1
    while pow10 <= p:
        pow10 *= 10

    pow10 /= 10

    while pow10 > 1:
        if not is_prime(s, p % pow10):
            return False
        pow10 /= 10
    return True

def main():
    # find the sum of the only 11 truncatable primes
    CAP = 1000000
    s, primes = gen_sieve(CAP)
    # have to end with 3, 7
    truncs = []

    for p in primes:
        if p < 10 or (p % 10 != 3 and p % 10 != 7):
            continue
        if trunc(s, p):
            truncs.append(p)

    print len(truncs), truncs, sum(truncs)

if __name__ == '__main__':
    main()
