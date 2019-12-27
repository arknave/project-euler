# all numbers - numbers divisible by 4 - div by 9 - div by 25 + div by 36

CAP = 2**50
SQ = 2**25
mob = [1 for _ in range(SQ)]
prime = [True for _ in range(SQ) ]

ans = CAP
for i in range(2, SQ):
    if mob[i] == 0:
        continue

    if prime[i]:
        for j in range(i, SQ, i):
            mob[j] = -mob[j]
            prime[j] = False
        for j in range(i * i, SQ, i * i):
            mob[j] = 0

    ans += mob[i] * (CAP // (i * i))

print(ans)
print(mob[:100])
