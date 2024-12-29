import math

MOD = int(1e9) + 123

def print_mat(a, n):
    for i in range(0, len(a), n):
        print(a[i:i+n])

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


def mat_pow_sum(a, e, n):
    """
    Computes A^0 + A^1 + ... + A^(n - 1)
    """
    assert e >= 1
    if e == 1:
        return identity(n)
    elif e % 2 == 1:
        return mat_sum(mat_exp(a, e - 1, n), mat_pow_sum(a, e - 1, n))
    else:
        h = e // 2
        sub = mat_pow_sum(a, h, n)
        scale = mat_exp(a, h, n)
        return mat_sum(sub, mat_mul(scale, sub, n))


def solve_slow(n):
    """
    Iterate over how many odd digits you want to use
    Then your state is (# of even with even freq, # of odd with odd freq)
    Fix the first digit, then matmul from (x, 0) to (x, y)
    How many states can there be? only 36 total?
    """
    NUM_STATES = 36

    def idx(e, o):
        return 6 * e + o

    # iterate over all masks of odd digits
    ans = 0
    for odds in range(6):
        digit_choice = math.comb(5, odds)
        vec = [0 for _ in range(NUM_STATES)]
        # start with an even digit: 2, 4, 6, 8
        vec[idx(4, 0)] += 4

        # start with an odd digit:
        if odds:
            vec[idx(5, 1)] += odds

        # iterate
        for l in range(1, n + 1):
            # print("slow", odds, l, digit_choice, vec[idx(5, odds)])
            cur = digit_choice * vec[idx(5, odds)]
            ans += cur

            nxt = [0 for _ in range(NUM_STATES)]
            for e in range(6):
                for o in range(6):
                    src = idx(e, o)

                    # append an even digit that's already even
                    if e:
                        nxt[idx(e - 1, o)] += e * vec[src]
                    # append an even digit that's not even
                    if e + 1 <= 5:
                        nxt[idx(e + 1, o)] += (5 - e) * vec[src]

                    # append an odd digit that's already odd
                    if o:
                        nxt[idx(e, o - 1)] += o * vec[src]
                    if o + 1 <= odds:
                        nxt[idx(e, o + 1)] += (odds - o) * vec[src]
            vec = [x % MOD for x in nxt]

    return ans % MOD


def solve_faster(n):
    def idx(e, o):
        return 6 * o + e

    ans = 0
    for odds in range(6):
        digit_choice = math.comb(5, odds)

        num_states = 6 * (odds + 1)

        vec = [0 for _ in range(num_states)]
        # start with an even digit: 2, 4, 6, 8
        vec[idx(4, 0)] += 4

        # start with an odd digit:
        if odds:
            vec[idx(5, 1)] += odds

        mat = [0 for _ in range(num_states * num_states)]
        for e in range(6):
            for o in range(odds + 1):
                src = idx(e, o)
                if e:
                    mat[num_states * idx(e - 1, o) + src] += e
                if e + 1 <= 5:
                    mat[num_states * idx(e + 1, o) + src] += 5 - e
                if o:
                    mat[num_states * idx(e, o - 1) + src] += o
                if o + 1 <= odds:
                    mat[num_states * idx(e, o + 1) + src] += odds - o

        """
        naive_sum = [0 for _ in mat]
        cur = identity(num_states)
        for l in range(1, n + 1):
            naive_sum = mat_sum(naive_sum, cur)
            cur = mat_mul(cur, mat, num_states)
        """

        fast_sum = mat_pow_sum(mat, n, num_states)
        # assert naive_sum == fast_sum

        ans += digit_choice * mat_vec_mul(fast_sum, vec, num_states)[idx(5, odds)]

    return ans % MOD


def main():
    ans = 0
    for u in range(1, 40):
        ans += solve_faster(1 << u)
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()
