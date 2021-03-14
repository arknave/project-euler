CAP = 999999
fact = [1]
for i in range(1, 10):
    fact.append(fact[-1] * i)
ans = sum(x for x in range(3, CAP) if sum(fact[int(y)] for y in str(x)) == x)
print(ans)
