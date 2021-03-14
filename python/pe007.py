from math import ceil, sqrt

def is_prime(n):
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

num = 1
test = 1
while num <= 10000:
    test += 2
    if is_prime(test):
        num += 1

print(test)
