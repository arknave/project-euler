def gen_primes(n):
    # returns a lit of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return primes

memo = {}
def count(primes, a, b):
    if a == 0:
        return 1
    elif a == 1:
        return 0

    if b < 0:
        return 0

    if primes[b] > a:
        return count(primes, a, b - 1)

    d = 0
    ans = 0
    while d * primes[b] <= a:
        ans += count(primes, a - d * primes[b], b - 1)
        d += 1

    memo[(a, b)] = ans

    return ans

def main():
    primes = gen_primes(int(1e6))
    ptr = 0
    v = 1
    while True:
        if primes[ptr] <= v:
            ptr += 1
        if count(primes, v, ptr) > 5000:
            print(v)
            break

        v += 1

main()
