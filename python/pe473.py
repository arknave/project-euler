from fractions import Fraction as Q

class Algebraic:
    """
    a + b sqrt(ROOT)
    """
    ROOT = 5
    def __init__(self, a, b = 0):
        self.a = Q(a)
        self.b = Q(b)

    def __repr__(self):
        return f"{self.a} + {self.b} sqrt({self.ROOT})"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))

    def conj(self):
        return Algebraic(self.a, -self.b)

    def __add__(self, other):
        return Algebraic(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Algebraic(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Algebraic(self.a * other.a + self.b * other.b * self.ROOT, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        """
        (a + bx) / (c + dx)
        (a + bx) * (c - dx) / (c + dx) (c - dx)
        (a + bx) * (c - dx) / c^2 - (d)x^2
        """
        mag = other * other.conj()
        assert mag.b == 0

        tmp = self * other.conj()
        tmp.a /= mag.a
        tmp.b /= mag.a

        return tmp

    def __pow__(self, k):
        res = Algebraic(1, 0)
        cur = self
        while k > 0:
            if k % 2 == 1:
                res = res * cur
            k //= 2
            cur = cur * cur

        return res

def main():
    phi = Algebraic(Q(1, 2), Q(1, 2))
    inv = Algebraic(1, 0) / phi

    """
    digits = [phi**(n - 1) + inv**n for n in range(2, 20)]
    dp = {(Algebraic(0), -10, "0.0")}
    for i, d in enumerate(digits):
        dp = {(x, last, "0" + rep + "0") for (x, last, rep) in dp} | {(x + d, i, "1" + rep + "1") for (x, last, rep) in dp if last + 1 != i}

    ans = 1
    for x, _, rep in dp:
        if x.b == 0 and int(x.a) == x.a:
            if 0 < x.a <= 1000:
                print(str(x.a).zfill(3), rep)
                ans += x.a

    for x in range(5, 100, 2):
        y = phi**x + inv**(x + 1) + phi**(x - 3) + inv**(x - 2)
        print(x, y)
    """
    # count, sum
    dp = [(0, 0), (1, 2), (1, 2), (1, 2), (1, 2)]
    for x in range(5, 100):
        if x % 2 == 1:
            y = phi**x + inv**(x + 1) + phi**(x - 3) + inv**(x - 2)
            assert y.b == 0
            y = y.a
            assert y.denominator == 1
            y = int(y)
            print(y)
            if y > 10**10:
                break

            p = x - 5
            new_count = dp[-1][0] + dp[p][0] + 1
            new_sum = dp[-1][1] + dp[p][1] + y * (dp[p][0] + 1)
            dp.append((new_count, new_sum))
        else:
            dp.append(dp[-1])

    print(dp)
    print(dp[-1][-1] + 1)


if __name__ == "__main__":
    main()
