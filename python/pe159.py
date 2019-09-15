CAP = 1000000
drs = list(range(CAP))
for i in range(10, CAP):
    x = sum(map(int, str(i)))
    drs[i] = drs[x]

mdrs = list(drs)
for i in range(2, CAP):
    for j in range(2 * i, CAP, i):
        mdrs[j] = max(mdrs[j], drs[i] + mdrs[j // i])

print(mdrs[24])
print(mdrs[961])
print(sum(mdrs[2:]))
