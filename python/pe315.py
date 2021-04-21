import itertools

def gen_primes(n):
    # returns a list of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return primes


SEGS = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
DISP = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1110010, 0b1111111, 0b1111011]
PC = [0] * (1 << 7)

for pc, m in zip(SEGS, DISP):
    assert pc == bin(m).count('1')

for x in range(1, 1 << 7):
    PC[x] = 1 + PC[x ^ (x & -x)]

def sam_clock(n):
    ans = 0
    while True:
        x = 0
        on = n
        while n > 0:
            d = n % 10
            ans += SEGS[d]
            x += d
            n //= 10

        if on == x:
            break
        else:
            n = x

    return 2 * ans


def max_clock(n):
    ans = 0

    last_disp, disp = [], []
    while True:
        x = 0
        on = n
        last_disp, disp = disp, []
        while n > 0:
            d = n % 10
            disp.append(DISP[d])
            x += d
            n //= 10

        for a, b in itertools.zip_longest(last_disp, disp, fillvalue=0):
            ans += PC[a ^ b]

        if on == x:
            break
        else:
            n = x

    # include whatever's in disp
    for d in disp:
        ans += PC[d]

    return ans


def main():
    # swap with seg sieve if needed
    lo, hi = int(1e7), int(2e7)
    primes = gen_primes(hi)

    ans = 0
    for p in primes:
        if lo <= p:
            print(p)
            ans += sam_clock(p) - max_clock(p)

    print(ans)


if __name__ == "__main__":
    main()
