import math
import heapq


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


def ctz(n):
    res = 0
    while n % 2 == 0:
        res += 1
        n >>= 1

    return res

def main():
    # Say a number is factored as p1^e1 p2^e2 ...
    # Then the number of divisors is (e1 + 1) (e2 + 1) ...
    # (e1 + 1) (e2 + 1) ... = 2^k
    # (2^i - 1 + 1) (2^j - 1 + 1)
    # start with 1 of each prime
    # can get rid of the largest prime for 2 2s 
    # when you do that, add a new option to get rid of a prime for 4 2s, or 2 3s
    # continue until you can no longer take options

    k = 500500
    primes = gen_primes(50 * k)
    ans = [1 for _ in range(k)]
    opts = [(2 * math.log(primes[i]), i, 2) for i in range(k)]
    while opts and opts[0][0] < ans[-1] * math.log(primes[len(ans) - 1]):
        assert ans[-1] == 1
        ans.pop()
        x, b, e = heapq.heappop(opts)
        ans[b] += e
        heapq.heappush(opts, (2 * x, b, 2 * e))

    MOD = 500_500_507
    # exp = 0
    res = 1
    for p, e in zip(primes, ans):
        res *= pow(p, e, MOD)
        res %= MOD
        # exp += ctz(e + 1)

    # assert exp == k
    print(res)

if __name__ == "__main__":
    main()
