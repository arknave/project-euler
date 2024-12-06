import itertools
import functools

MOD = 1005075251

pass_thru = lambda x, y: True
ops = [
    (lambda a, b: a + b, pass_thru),
    (lambda a, b: a - b, pass_thru),
    (lambda a, b: a * b, pass_thru),
    (lambda a, b: a // b, lambda a, b: b != 0 and a % b == 0),
]

def get_score(x, flag):
    return 0 if flag else x

@functools.lru_cache(maxsize=1<<20)
def score(goal, vals, used=0):
    if (goal, 1) in vals:
        return used
    if len(vals) <= 1:
        return MOD

    ans = MOD
    n = len(vals)
    for i, j in itertools.permutations(range(n), 2):
        if i < j:
            lo, hi = i, j
        else:
            lo, hi = j, i
        new_vals = vals[:lo] + vals[lo+1:hi] + vals[hi+1:]
        for op, check in ops:
            if check(vals[i][0], vals[j][0]):
                res = op(vals[i][0], vals[j][0])
                new_score = used + get_score(*vals[i]) + get_score(*vals[j])
                if new_score < ans:
                    ans = min(ans, score(goal, new_vals + ((res, 1),), new_score))

    return ans


def main():
    with open("../data_files/p828_number_challenges.txt", "r") as fin:
        lines = fin.readlines()

    ans = 0
    for i, line in enumerate(lines):
        goal, nums = line.strip().split(':')
        goal = int(goal)
        nums = tuple((int(x), 0) for x in nums.split(','))

        cur = score(goal, nums)
        ans += pow(3, i + 1, MOD) * cur % MOD
        ans %= MOD

    print(ans)

if __name__ == '__main__':
    main()
