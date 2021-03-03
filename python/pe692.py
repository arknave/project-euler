from functools import lru_cache

@lru_cache()
def win(n, k):
    # n is number of pebbles left, k is max you can take
    assert k <= n
    if n == 0:
        return False

    for x in range(1, k + 1):
        if not win(n - x, min(n - x, 2 * x)):
            return True

    return False

def h(n):
    for k in range(1, n):
        if win(n, k):
            return k

    return n

def merge(x, y):
    res = {}
    for k, v in y.items():
        res[k] = x.get(k, 0) + v

    return res

def main():
    # Brute force shows that the h(x) is the smallest
    # term in the fibonacci representation of x
    # e.g. 64 = 55 + 8 + 1, so h(64) = 1

    # The sequence looks very nice...
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 1 5
    # 1 2 3 1 5 1 2 8
    # 1 2 3 1 5 1 2 8 1 2 3 1 13
    # 1 2 3 1 5 1 2 8 1 2 3 1 13 1 2 3 1 5 1 2 21


    # Take the last sequence, append the second to last sequence, and fix the last term
    N = 23416728348467685
    # N is the 80th fibonacci number, so this should be easy

    a, b = 1, 2
    fa, fb = {1: 1}, {1: 1, 2: 1}
    while b != N:
        fa, fb = fb, merge(fa, fb)
        fb[a] -= 1
        fb[a + b] = 1

        a, b = b, a + b

    print(sum(k * v for k, v in fb.items()))

if __name__ == "__main__":
    main()
