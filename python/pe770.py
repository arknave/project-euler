from functools import lru_cache
from fractions import Fraction
import math

@lru_cache(maxsize=None)
def solve(takes, gives):
    if gives == 0:
        return Fraction(1, 1)
    elif takes == 0:
        return Fraction(2, 1) * solve(takes, gives - 1)
    else:
        # find the value of p s.t. 
        # (1 - p) * f(t - 1, g) == (1 + p) * f(t, g - 1)
        # x - xp = y + yp
        # x - y = (x + y) p
        # p = (x - y) / (x + y)
        x = solve(takes - 1, gives)
        y = solve(takes, gives - 1)
        return 2 * x * y / (x + y)

def main():
    # printing and pattern matching
    for n in range(1, 20):
        f = solve(n, n)
        g = Fraction(4**n, (4**n + math.comb(2 * n, n)) // 2)
        assert f == g
        print(n, float(f), math.log(float(f)))

    """
    2 * 4^n / (4^n + (2n choose n)) >= goal
    2 * 4^n >= goal * 4^n + goal (2n choose n)
    2 * 4^n >= goal * 4^n + goal (2n choose n)
    (2 - goal) * 4^n >= goal (2n choose n)
    4^n / (2n choose n) >= goal / (2 - goal)
    4^n n! n! / (2n)! >= goal / (2 - goal)
    """
    ans = 0
    cur = 1.0
    for goal in [1.7, 1.9, 1.9999]:
        g = goal / (2.0 - goal)
        while cur < g:
            ans += 1
            cur *= 2.0
            cur *= ans
            cur /= 2 * ans - 1.0
        print(goal, ans)

if __name__ == "__main__":
    main()
