import itertools
import math

def solve(m):
    """
    Iterate over every quadrilateral. Then Pick's theorem gives

    A = I + B/2 - 1

    Where A is the area of the shape, I is the number of lattice points
    in the interior and B is the number of points on the border. A and B
    can be computed in constant time, so we can compute I in constant time as
    well.

    2 A - B + 2 = 2 I
    """
    squares = set(x * x for x in range(1, m * m))
    sq = 0
    gcds = [[math.gcd(x, y) for x in range(m + 1)] for y in range(m + 1)]

    for a, b, c, d in itertools.product(range(1, m + 1), repeat=4):
        area, border = 0, 0
        for adj in [(a, b), (b, c), (c, d), (d, a)]:
            # double area
            area += adj[0] * adj[1]
            border += gcds[adj[0]][adj[1]]

        interior = (area - border + 2) // 2
        sq += interior in squares

    print(sq)


def main():
    solve(100)


if __name__ == "__main__":
    main()
