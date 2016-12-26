CAP = 10000
def gen_primes():
    is_prime = [x % 2 == 1 for x in range(CAP)]
    is_prime[2] = True
    
    primes = []
    for i in range(3, CAP, 2):
        if is_prime[i]:
            if i != 5:
                primes.append(i)

            for j in range(i * i, CAP, 2 * i):
                is_prime[j] = False

    return primes


def is_prime(x):
    if x % 2 == 0:
        return False
    j = 3
    while j * j <= x:
        if x % j == 0:
            return False
        j += 2

    return True


def works(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


def main():
    primes = gen_primes()
    l = len(primes)
    for i in range(l):
        for j in range(i + 1, l):
            if works(primes[i], primes[j]):
                for k in range(j + 1, l):
                    if all(works(primes[x], primes[k]) for x in (i, j)):
                        for n in range(k + 1, l):
                            if all(works(primes[x], primes[n]) for x in (i, j, k)):
                                for m in range(n + 1, l):
                                    if all(works(primes[x], primes[m]) for x in (i, j, k, n)):
                                        out = [primes[x] for x in [i, j, k, n, m]]
                                        print(out, sum(out))
                                        return

main()
