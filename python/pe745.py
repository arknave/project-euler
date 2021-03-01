from math import sqrt

def S(N):
    rt = int(sqrt(N))
    while rt * rt <= N:
        rt += 1

    f = [0] + [N // x // x for x in range(1, rt)]

    for x in range(rt - 1, 0, -1):
        for k in range(x + x, rt, x):
            f[x] -= f[k]

    return sum(i * i * v for i, v in enumerate(f))

def main():
    """
    Let g(n) be the maximum square that divides n.

    Let S(N) = \sum_{i = 1}^N g(n).
    Find the sum of g(n) over the range 1 <= 10**14

    Solution:
    For each x 1 <= x <= sqrt(N), let f(x) be the 
    count of numbers where g(n) = x. This can be done
    with inclusion-exclusion?

    I think a first pass is
    f(x) = (N // x // x) - f(k x) for k in range(2 .. N)
    This looks O(x log x)?
    """
    MOD = int(1e9 + 7)
    for N in [10, 100, 10**14]:
        print(N, S(N) % MOD)



if __name__ == "__main__":
    main()
