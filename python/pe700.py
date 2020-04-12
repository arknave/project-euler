x = 1504170715041707
m = 4503599627370517

a = [x]

# Solution by radeye
# not quite sure why this works
lo = x
hi = x
while lo > 0:
    v = (lo + hi) % m
    lo = min(lo, v)
    hi = max(hi, v)
    if lo < a[-1]:
        a.append(lo)

print(a)
print(sum(a))

"""
# this is the slow sqrt(m) code I originally submitted with.

ix = pow(x, m - 2, m)

SQRT = int(7e7)

a = [x]

c = x
while a[-1] > SQRT:
    c += x
    if c >= m:
        c -= m
    if c < a[-1]:
        a.append(c)

print(a)

# now, figure out where in the seqence everything appears
b = [(v * ix % m, v) for v in range(1, a[-1])]
b.sort()

for idx, v in b:
    if v < a[-1]:
        a.append(v)

print(a)
print(sum(a))
"""
