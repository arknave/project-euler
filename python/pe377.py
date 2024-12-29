import functools

@functools.cache
def brute(n):
    """
    Return the count and sum of numbers with digit sum n
    """
    if n == 0:
        return 1, 0

    count = 0
    ans = 0
    for d in range(1, min(n + 1, 10)):
        c, s = brute(n - d)
        count += c
        ans += s * 10 + d * c

    return count, ans

def identity(n):
    res = [0 for _ in range(n * n)]
    for i in range(n):
        res[n * i + i] = 1

    return res


def mat_sum(a, b):
    assert len(a) == len(b)
    return [x + y for x, y in zip(a, b)]


def mat_vec_mul(a, b, n):
    c = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i] += a[n * i + j] * b[j]

    return c

MOD = int(1e9)

def mat_mul(a, b, n):
    c = [0 for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[n * i + j] += a[n * i + k] * b[n * k + j] % MOD
                if c[n * i + j] >= MOD:
                    c[n * i + j] -= MOD

    return c


def mat_exp(a, e, n):
    res = identity(n)
    while e > 0:
        if e % 2 == 1:
            res = mat_mul(res, a, n)

        a = mat_mul(a, a, n)
        e //= 2

    return res


def main():
    # 10 counts, 10 sums
    n = 20
    state = [0 for _ in range(n)]
    state[9] = 1
    mat = [0 for _ in range(n * n)]

    # Set up count matrix
    for i in range(9):
        mat[n * i + (i + 1)] = 1
    for x in range(1, 10):
        mat[n * 9 + x] = 1

    # Set up sums matrix
    for i in range(10, 19):
        mat[n * i + (i + 1)] = 1
    for x in range(1, 10):
        mat[n * 19 + x] = 10 - x
    for x in range(11, 20):
        mat[n * 19 + x] = 10

    ans = 0
    for i in range(1, 18):
        t = mat_exp(mat, 13**i, n)
        res = mat_vec_mul(t, state, n)
        print(i, 13**i, res[19])
        ans += res[19]
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()
