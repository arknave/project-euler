from fractions import Fraction

def gen_row(a, b):
    return [Fraction(a**x, 1) for x in range(b)]

def gen_matrix(n):
    return [gen_row(i, n) for i in range(1, n + 1)]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def scale(v, row):
    return [v * x for x in row]

def inverse(mat):
    n = len(mat)
    aug = []
    for i, row in enumerate(mat):
        zero = [Fraction(0, 1)] * n
        zero[i] = Fraction(1, 1)
        aug.append(row + zero)

    for i in range(n):
        aug[i] = list(scale(1 / aug[i][i], aug[i]))
        for j in range(n):
            if i == j:
                continue

            aug[j] = [x - y for x, y in zip(aug[j], scale(aug[j][i], aug[i]))]

    inv = [row[n:] for row in aug]
    return inv

def get_coeffs(values):
    n = len(values)
    mat = gen_matrix(n)

    inv = inverse(mat)
    out = [dot(row, values) for row in inv]

    return out

def eval_poly(coeffs, x):
    return dot(coeffs, gen_row(x, len(coeffs)))

def main():
    poly = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    ans = 0
    for i in range(1, 11):
        values = [eval_poly(poly, x) for x in range(1, i + 1)]
        coeffs = get_coeffs(values)

        for x in range(1, 100):
            if eval_poly(poly, x) != eval_poly(coeffs, x):
                ans += eval_poly(coeffs, x)
                break
        else:
            print('Found exact at', i)

    print(ans)

main()
