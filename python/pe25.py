def mat_mult(a, b):
    # a and b are 2x2 matrices
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

def mat_pow(a, n):
    # a is a 2x2 matrix. n is the integer power to raise to.
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return a
    elif n % 2 == 0:
        return mat_pow(mat_mult(a, a), n // 2)
    else:
        return mat_mult(a, mat_pow(mat_mult(a, a), n // 2))

def fib(n):
    # return the nth fibonacci number where fib(1) = 1 and fib(2) = 1
    mat = [[0, 1], [1, 1]]
    return mat_pow(mat, n)[1][0]

def main():
    # find the index of the smallest fibonacci number with 1000 digits, if f(0) = 0, f(1) = 1, f(2) = 1
    lo = 1
    hi = 2
    while len(str(fib(hi))) < 1000:
        lo, hi = hi, 2 * hi

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if len(str(fib(mid))) < 1000:
            lo = mid
        else:
            hi = mid

    print(hi)

if __name__ == '__main__':
    main()
