from functools import reduce
import itertools

def main():
    # 1/x + 1/y = 1/n
    # nx + ny = xy
    # 0 = xy - nx - ny
    # n^2 = xy - nx - ny + n^2
    # n^2 = (x - n) (y - n)
    # Number of pairs is thus equivalent to number of factors of n^2 <= n
    # number of small factors = (number of factors + 1) // 2
    # Find the smallest n where n^2 has >= 1999 factors
    # given the prime factorization of a number p1^e1 p2^e2 ...
    # the pf of its square is p1^2e1 p2^2e2
    # number of factors is (2e1 + 1) * (2e2 + 1) * ...
    # now, say all e1 = 1, then we have 3 
    # whats log base 3 of 8M? 14 or 15
    # So only consider the first 14 or 15 primes, then do the thing
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    goal = 2 * 4000000 - 1
    ans = float('inf')
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for d in range(1, 5):
                    n = 1
                    for p, e in zip(primes, [a, b, c, d]):
                        n *= (p**e)

                    num_div = (2 * a + 1) * (2 * b + 1) * (2 * c + 1) * (2 * d + 1)
                    ptr = 4
                    while ptr < len(primes) and num_div < goal:
                        n *= primes[ptr]
                        num_div *= 3
                        ptr += 1

                    if num_div >= goal:
                        ans = min(ans, n)
    print(ans)

main()
