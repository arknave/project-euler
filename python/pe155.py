from fractions import Fraction


def solve(n):
    memo = [None, set([Fraction(1)])]

    for k in range(2, n + 1):
        res = []
        for a in range(1, (k // 2) + 1):
            b = k - a
            assert a <= b
            for x in memo[a]:
                for y in memo[b]:
                    res.append(x + y)
                    res.append(1 / ((1 / x) + (1 / y)))
        memo.append(set(res))
        print(k, len(memo[k]))

    return len(set.union(*memo[1:]))


def main():
    print(solve(18))


if __name__ == "__main__":
    main()
