def prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for d in range(3, x, 2):
        if d * d > x:
            break
        if x % d == 0:
            return False
    return True

def main():
    # ignore the innermost rings. Figure out behaviour when they get large
    # Can't be on an edge, must be on a corner. This is because distances in same ring are +1, -1, and neither are prime.
    # Also can't be any corner. For example, distances from a corner are 6k, which is not prime, so PD is limited to 2
    # That means the only candiates are along the top ring: 1, 2, 7, 8, 19, 20, 37, etc.
    # For a member of the top ring, we can compute it as 2, 8, 20, 38, (2 + \sum 6k)
    # The differences of a top ring value (v) in ring k are:
    # 6k
    # 6k + 1
    # 1
    # 6(k - 1)
    # 6k - 1
    # 6k + 6(k + 1) - 1
    # only have to check these 3 values

    # The differences of the last value in each ring (v, k) are
    # (19, 2)
    # 6(k + 1)
    # 6(k + 1) - 1
    # 1
    # 6k
    # 12k - 7
    # 6k - 1

    cur = 8
    k = 2
    ans = [1, 2]
    while len(ans) < 2000:
        vals = [6 * k + 1, 6 * k - 1, 12 * k + 5]
        if all(prime(v) for v in vals):
            ans.append(cur)
            
        last = cur + 6 * k - 1
        diffs = [6 * (k + 1) - 1, 12 * k - 7, 6 * k - 1]
        if all(prime(v) for v in diffs):
            ans.append(last)
        cur += 6 * k
        k += 1

    print(ans[1999])

main()
