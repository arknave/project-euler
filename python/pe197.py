def f(x):
    return int(pow(2, 30.403243784 - x * x)) * 1e-9

u = [-1.0]
while len(u) < 3 or u[-3] != u[-1]:
    x = f(u[-1])
    u.append(x)

print(sum(u[-2:]))
