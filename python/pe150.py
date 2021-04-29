import math

def s():
    MASK = (1 << 20) - 1
    OFFSET = 1 << 19
    t = 0
    while True:
        t = (615949 * t + 797807) & MASK
        yield t - OFFSET


def gen_case(n=1000):
    table = []
    gen = s()
    for row_id in range(n):
        row = []
        for col in range(row_id + 1):
            row.append(next(gen))

        table.append(row)

    return table


def build_vals(table, r, c):
    vals = []
    for k in range(r, len(table)):
        d = k - r + 1
        vals.append(sum(table[k][c:c+d]))

    return list(reversed(vals))



def brute(table):
    ans = math.inf
    n = len(table)
    for i in range(n):
        for j in range(i + 1):
            vals = []
            cur = 0
            for k in range(i, n):
                d = k - i + 1
                vals.append(sum(table[k][j:j+d]))
                cur += vals[-1]
                ans = min(ans, cur)

    return ans


def solve_2d(table):
    """
    Reduce this to a 1d problem, then find the min prefix sum
    To keep things "simple", iterate very strangely: right-to-left, bottom to top
    Each time you encounter a new element, have to add a new value to all elements in the array (O(N)), then find min prefix (also O(N))
    Overall runtime: O(n^3).
    """
    n = len(table)
    for exp, row in enumerate(table, start=1):
        assert len(row) == exp

    ans = math.inf
    for j in range(n - 1, -1, -1):
        vals = []
        for i in range(n - 1, j - 1, -1):
            for k in range(i + 1, n):
                d = k - i
                vals[-d] += table[k][j + d]
            vals.append(table[i][j])

            # assert vals == build_vals(table, i, j)
            pref = 0
            for x in reversed(vals):
                pref += x
                ans = min(ans, pref)

    return ans


def main():
    case = [[15], [-14, -7], [20, -13, -5], [-3, 8, 23, -26], [1, -4, -5, -18, 5], [-16, 31, 2, 9, 28, 3]]
    case = gen_case()
    # print(case)
    print(solve_2d(case))
    # print(brute(case))

if __name__ == "__main__":
    main()
