from math import ceil, sqrt

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve(n):
    res = 1
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0 and is_prime(i):
            res = max(res, i)
    return res

print(solve(600851475143))
