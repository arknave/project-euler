import functools

def solve(n):
    s = str(n)

    @functools.cache
    def inner(idx, dig_sum, is_free):
        """
        return (count, sum)
        """
        if idx == len(s):
            return (0, 0) if dig_sum > 0 else (1, 0)

        cur = int(s[idx])
        up = 9 if is_free else cur
        up = min(up, dig_sum)
        ans = [0, 0]
        for digit in range(up + 1):
            sub = inner(idx + 1, dig_sum - digit, is_free or digit < cur)
            ans[0] += sub[0]
            ans[1] += sub[1]
            ans[1] += digit * pow(10, len(s) - 1 - idx) * sub[0]

        return tuple(ans)

    ans = 0.0
    for dig_sum in range(1, len(s) * 9 + 1):
        _, val_sum = inner(0, dig_sum, False)
        ans += val_sum / dig_sum

    return ans

for n in [10, 123, 12345, 1234567890123456789]:
    print(n, solve(n))
