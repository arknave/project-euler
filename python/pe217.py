def brute(n):
    ans = 0
    for x in range(10 ** n):
        s = str(x)
        h = (len(s) + 1) // 2
        fh = s[:h]
        sh = s[-h:] if len(s) % 2 == 0 else s[-h:]
        if sum(int(c) for c in fh) == sum(int(c) for c in sh):
            ans += x

    return ans


def fast(n):
    k = n // 2
    max_sum = 9 * k

    p10 = [pow(10, i) for i in range(n + 1)]

    # cnt[i][j] number of ways to sum to i using j digits, leading 0s allowed
    cnt = [[0 for _ in range(k + 1)] for _ in range(max_sum + 1)]
    cnt[0][0] = 1

    for s in range(max_sum + 1):
        for j in range(k):
            for d in range(10):
                if s + d <= max_sum:
                    cnt[s + d][j + 1] += cnt[s][j]

    ans = 45
    for l in range(2, n + 1):
        h = l // 2
        repunit = sum(p10[:h])
        offset = p10[(l + 1) // 2]
        for s in range(1, max_sum + 1):
            # average digit is s / h
            # average number is s / h * 11111...
            # sum of numbers is thus s / h * 11111 * total
            cnt0 = cnt[s][h]
            cnt1 = cnt[s][h] - cnt[s][h - 1]
            rhs = (s * cnt0 * repunit) // h

            if h == 1:
                lhs = rhs
            else:
                lhs = rhs - (s * cnt[s][h - 1] * (repunit - 1) // 10) // (h - 1)

            term = lhs * offset * cnt0 + rhs * cnt1
            # print("sum, digits, cnt1, cnt0, lhs, rhs", s, h, cnt1, cnt0, lhs, rhs, term)
            if l % 2 == 0:
                ans += term
            else:
                # print(term * 10, cnt0 * cnt1 * 45 * offset // 10)
                ans += 10 * term
                ans += cnt0 * cnt1 * 45 * offset // 10

    return ans


def main():
    MOD = 3 ** 15
    ans = fast(47)
    print(ans % MOD)
    for n in range(2, 10):
        print(n, fast(n), brute(n))


if __name__ == "__main__":
    main()
