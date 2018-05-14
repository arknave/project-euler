from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    n = int(input())
    res = 1
    for x in range(2, n + 1):
        res = lcm(res, x)

    print(res)

T = int(input())
for _ in range(T):
    main()
