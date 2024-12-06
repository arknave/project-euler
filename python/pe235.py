def u(r, k):
    return (900.0 - 3.0 * k) * pow(r, k - 1)

def s(r, n=5000):
    return sum(u(r, k) for k in range(1, n + 1))

lo = 1.0
hi = 1.003
target = -600_000_000_000

assert s(hi) < target < s(lo)
for _ in range(200):
    mid = (lo + hi) * 0.5
    if s(mid) < target:
        hi = mid
    else:
        lo = mid

print(f"{lo:.12}")
