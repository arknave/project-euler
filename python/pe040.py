def get_dig(x, p):
    for _ in range(p):
        x //= 10
    return x % 10
def k_th(k):
    """Returns the kth digit if 12345678910111213.."""
    p = 10
    cur_len = 1
    while cur_len * (p - (p // 10)) <= k:
        k -= cur_len * (p - (p // 10))
        p *= 10
        cur_len += 1

    val = p // 10 + k // cur_len
    dig = k % cur_len
    return get_dig(val, cur_len - dig - 1)

ans = 1
i = 1
while i <= 1000000:
    ans *= k_th(i - 1)
    i *= 10

print(ans)
