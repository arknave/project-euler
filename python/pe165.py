from fractions import Fraction as Q
import itertools

def t():
    s = 290797
    while True:
        s *= s
        s %= 50515093
        yield s % 500

def sgn(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def ccw(a, b, c):
    return cross(sub(b, a), sub(c, a))

def isect(seg0, seg1):
    a_side = ccw(seg1[0], seg1[1], seg0[0])
    b_side = ccw(seg1[0], seg1[1], seg0[1])
    c_side = ccw(seg0[0], seg0[1], seg1[0])
    d_side = ccw(seg0[0], seg0[1], seg1[1])

    if sgn(a_side) * sgn(b_side) == -1 and sgn(c_side) * sgn(d_side) == -1:
        den = b_side - a_side
        x = seg0[0][0] * b_side - seg0[1][0] * a_side
        y = seg0[0][1] * b_side - seg0[1][1] * a_side

        return (Q(x, den), Q(y, den))

    return None

def main():
    n = 5000
    ts = list(itertools.islice(t(), 4 * n))

    pts = set()
    for i in range(n):
        a0, b0, c0, d0 = ts[(4 * i):(4 * (i + 1))]
        for j in range(i + 1, n):
            a1, b1, c1, d1 = ts[(4 * j):(4 * (j + 1))]
            pt = isect(((a0, b0), (c0, d0)), ((a1, b1), (c1, d1)))
            if pt is not None:
                pts.add(pt)

    print(len(pts))


if __name__ == "__main__":
    main()
