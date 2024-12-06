import math

def does_terminate(x):
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5

    return x == 1

def main():
    s = 2
    ans = 0
    N = 10000
    for x in range(5, N + 1):
        while (s + 1) * (math.log(x) - math.log(s + 1)) > s * (math.log(x) - math.log(s)):
            s += 1

        g = math.gcd(x, s)
        if does_terminate(s // g):
            ans -= x
        else:
            ans += x

    print(ans)

if __name__ == "__main__":
    main()
