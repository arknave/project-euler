from math import gcd

def brute(m):
    squares = set(x * x for x in range(1000))

    ans = 0
    for c in range(1, m + 1):
        for b in range(1, c + 1):
            for a in range(1, b + 1):
                s = c * c + (a + b) * (a + b)
                if s in squares:
                    # print('Found', a, b, c)
                    ans += 1

    return ans

def divisors(x):
    yield 1

    if x == 1:
        return

    for d in range(2, x):
        if d * d > x:
            break
        if x % d == 0:
            yield d
            if d * d != x:
                yield x // d

def count_range(x, y):
    """
    Count the number of integers z such that
    1 <= z < y
    z <= x
    y - z <= x
    z <= y - z

    This implies the following
    y - z <= x
    -z <= x - y
    z >= y - x

    y - x <= z <= x
    1 <= z <= y - 1

    z <= y - z
    2z <= y
    z <= (y / 2)
    """
    return max(0, min(y - 1, x, y // 2) - max(1, y - x) + 1)

squares = {x * x: x for x in range(500)}

def for_leg(leg):
    ans = 0
    for k in divisors(leg):
        # print('Div', k)
        for b in range(1, leg + 1):
            # k * (a^2 - b^2) = leg
            a2 = (leg + k * b * b) // k
            if a2 in squares:
                a = squares[a2]

                if a > b and gcd(a, b) == 1 and (a + b) % 2 == 1:
                    leg2 = 2 * k * a * b
                    # print(a, b, 'gens', leg, leg2)
                    # print(count_range(leg, leg2), 'sols')

                    ans += count_range(leg, leg2)

            # 2 * k * a * b == leg
            if leg % (2 * k * b) == 0:
                a = leg // (2 * k * b)
                leg2 = k * (a * a - b * b)
                if a > b and gcd(a, b) == 1 and (a + b) % 2 == 1:
                    # print(a, b, 'gens', leg, leg2)
                    # print(count_range(leg, leg2), 'sols')
                    ans += count_range(leg, leg2)

    return ans

def main():
    # say the side lengths are a, b, c
    # for the sample, a b c = 6 5 3
    # then the possible paths are

    # sides a, b + c, with s2 = a^2 + b^2 + 2bc + c^2
    # sides b, a + c, with s2 = b^2 + a^2 + 2ac + c^2
    # sides c, a + b, with s2 = c^2 + a^2 + 2ab + c^2

    # Basically check if any of those are pythagorean triples
    # Ignoring rotations means a <= b <= c

    GOAL = 1000000
    ans = 0
    leg = 1
    while ans < GOAL:
        ans += for_leg(leg)
        leg += 1

    print(leg - 1)

main()
