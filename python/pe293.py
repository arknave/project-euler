primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
CAP = 10**9
dp = [[1]]

for i, p in enumerate(primes):
    dp.append([])
    for x in dp[-2]:
        y = x * p
        while y < CAP:
            dp[-1].append(y)
            y *= p

    dp[-1].sort()

admissible = []
for x in dp[1:]:
    admissible += x

def is_prime(v):
    if v < 2:
        return False
    if v == 2:
        return True
    if v % 2 == 0:
        return False
    for k in range(3, v, 2):
        if k * k > v:
            break

        if v % k == 0:
            return False

    return True

admissible.sort()
s = set()
for x in admissible:
    m = 2
    while not is_prime(x + m):
        m += 1
    print(x, m)
    s.add(m)

print(sum(s))
