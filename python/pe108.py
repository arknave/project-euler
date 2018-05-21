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
    # sieve all the numbers and count i guess
    CAP = 1000000
    GOAL = 1000
    NUM_DIV = 2 * GOAL - 1
    num_factors = [1 for _ in range(CAP + 1)]
    for d in range(2, CAP + 1):
        if num_factors[d] == 1:
            # d is a prime, do all of its powers
            v = d
            e = 1
            while v <= CAP:
                for j in range(v, CAP + 1, v):
                    num_factors[j] //= 2 * e - 1
                    num_factors[j] *=  2 * e + 1
                v *= d
                e += 1
        if num_factors[d] >= NUM_DIV:
            print(d)
            break

main()
