MOD = int(1e9 + 7)

def build_choose(n):
    res = [[1]]
    for _ in range(n):
        row = [1]
        for a, b in zip(res[-1], res[-1][1:]):
            c = a + b
            if c >= MOD:
                c -= MOD
            row.append(c)
        row.append(1)
        res.append(row)

    return res

def d(n):
    choose = build_choose(n + 1)

    # handle 1111, 22222... etc separately
    ans = n * 9
    for num_len in range(1, n + 1):
        for big in range(num_len // 2 + 1, num_len):
            # 1-9 case 
            for first_dig in [0, 1]:
                lead_opts = 1 if first_dig else 8
                cur = 9 * lead_opts * choose[num_len - 1][big - first_dig] * pow(9, num_len - 1 - (big - first_dig), MOD) % MOD
                ans += cur
                if ans >= MOD:
                    ans -= MOD

            if big < num_len:
                # zero case
                lead_opts = 9
                cur = lead_opts * choose[num_len - 1][big] * pow(9, num_len - 1 - big, MOD) % MOD
                ans += cur
                if ans >= MOD:
                    ans -= MOD

    return ans

for k in [4, 10, 2022]:
    print(k, d(k))
