def fib(n):
    a = [1, 2]
    while a[-1] <= n:
        a.append(a[-1] + a[-2])

    a.pop()
    return a

def dp1(a, S=None):
    if S is None:
        S = sum(a)

    dp = [0 for _ in range(S + 1)]
    dp[0] = 1
    for x in a:
        for i in range(S - x, -1, -1):
            dp[i + x] += dp[i]

    return dp

def dp2(a, N):
    vals = [(0, 1)]
    for x in a:
        nxt = [(v + x, t) for (v, t) in vals if v + x <= N]

        new_vals = []
        i, j = 0, 0
        while i < len(vals) and j < len(nxt):
            if vals[i][0] < nxt[j][0]:
                new_vals.append(vals[i])
                i += 1
            elif vals[i][0] > nxt[j][0]:
                new_valls.append(nxt[j])
                j += 1
            else:
                new_vals.append((vals[i][0], vals[i][1] + nxt[j][1]))
                i += 1
                j += 1

        new_vals += vals[i:]
        new_vals += nxt[j:]

        vals = new_vals

    return vals


def main():
    N = 10**13
    a = fib(N)
    k = 30
    lo, hi = a[:k], a[k:]
    # print(lo, hi)
    psum = dp1(lo)
    for i in range(1, len(psum)):
        psum[i] += psum[i - 1]

    vals = dp2(hi, N)

    ans = 0
    for v, t in vals:
        ans += t * psum[min(len(psum) - 1, N - v)]

    print(ans)

if __name__ == "__main__":
    main()
