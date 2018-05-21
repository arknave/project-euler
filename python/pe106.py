import itertools

def solve(n):
    inds = list(range(n))
    ans = 0
    for k in range(4, n + 1, 2):
        for combo in itertools.combinations(inds, k):
            for subcombo in itertools.combinations(combo, k // 2):
                remainder = [x for x in combo if x not in subcombo]
                has_big, has_small = False, False
                for a, b in zip(subcombo, remainder):
                    has_big = has_big or a > b
                    has_small = has_small or a < b

                if has_big and has_small:
                    ans += 1

    return ans // 2

def main():
    """
    assume if |B| > |C| then S(B) > S(C)
    only have to test sets of the same size to make sure you dont repeat
    never have to try size 1

    a b c d
    4 only test a + d, b + c

    f(4) = 1

    a b c d e
    test...
    a + d, b + c
    b + e, c + d
    a + e, c + d
    a + e, b + d
    a + e, b + c

    f(5) = (5 choose 4) * f(4) = 5 * 1 = 5

    a b c d e f
    f(6) = (6 choose 4) * 1 + (6 choose 6) * 5
         = 15 * 1 + 1 * 5
         = 20

    a b  no (d > b, c > a)
    a c  no (d > c, b > a)
    a d ???

    a b c  no (f > c, e > b, c > a)
    a b d  no (f > d, e > b, c > a)
    a b e  no (f > d, d > b, c > a)
    a b f ???
    a c d  no (f > d, e > c, b > a)
    a c e  no (f > e, d > c, b > a)
    a c f ???
    a d e ???
    a d f ???
    a e f ???

    general procedure:
    always take a, iterate on highest
    if you take last, can choose from remainder
    if you take second last, must take 3rd last, choose from remainder
    etc etc

    0 1 2 3 4 5
    5 -> 4 choose 1 = 4
    4, 3 -> 0 choose 0 = 1
    = 5

    0 1 2 3 4 5 6 7
    7 -> (6 choose 2) = 15
    6, 5 -> (4 choose 1) = 4
    5, 4, 3 -> 1
    = 20

    0 1 2 3 4 5 6 7 8 9
    9 -> (8 choose 3) = 56

    partial sums of (4 choose 1) + (6 choose 2) + (8 choose 3) + (10 choose 4) + (12 choose 5)...
    oh fuck are these catalans ???

    partial sums of 1, 4, 15, 56
    1 * 1
    2 * 2
    3 * 5
    4 * 14

    f(7) = (7 choose 4) * 1 + (7 choose 6) * 5
         = 35 * 1 + 7 * 5
         = 70

    """
    for x in range(4, 13):
        print(x, solve(x))

main()
