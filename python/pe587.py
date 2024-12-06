import math

def solve(n):
    slope = 1.0 / n

    # find the intersection point between this line and the circle.
    # That is, y = mx, (x - 1)^2 + (y - 1)^2 = 1
    # sub in y to get
    # (x - 1)^2 + (mx - 1)^2 = 1
    # x^2 - 2x + 1 + m^2 x^2 - 2mx + 1 = 1
    # (1 + m^2) x^2 - 2(1 + m)x + 1 = 0

    # [2(1 + m) +- sqrt(4(1 + m)^2 - 4 (1 + m^2))] / 2(1 + m^2)
    # [1 + m +- sqrt((1 + m)^2 - (1 + m^2))] / (1 + m^2)
    # [1 + m +- sqrt(2m)] / (1 + m^2)
    x = (1 + slope - math.sqrt(2.0 * slope)) / (1.0 + slope * slope)

    # area under the slope is easy
    tri = x * slope * x / 2.0
    curve = 0.0

    # area under the curve is a little more interesting.
    # maybe we can just riemann sum?
    # (x - 1)^2 + (y - 1)^2 = 1
    # (y - 1)^2 = 1 - (x - 1)^2
    # y = 1 + sqrt(1 - (x - 1)^2)
    DELTA = 0.0001
    while x < 1.0:
        y = 1.0 - math.sqrt(1.0 - (x - 1.0)**2)
        curve += DELTA * y
        x += DELTA

    num = tri + curve
    # den = (1 - pi / 4) r
    den = 1.0 - math.pi / 4.0
    return num / den

def main():
    lo = 1
    hi = 2

    TARGET = 0.001
    while solve(hi) > TARGET:
        lo = hi
        hi *= 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if solve(mid) > TARGET:
            lo = mid
        else:
            hi = mid
    
    print(hi)


if __name__ == "__main__":
    main()
