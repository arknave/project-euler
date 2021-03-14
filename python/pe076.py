memo = {}

def count(a, b):
    if b > a:
        return count(a, a)

    if b == 0:
        return 1 if a == 0 else 0

    if a <= 1:
        return 1

    if (a, b) in memo:
        return memo[(a, b)]

    ans = 0
    for i in range(1, b + 1):
        d = 1
        while d * i <= a:
            ans += count(a - d * i, i - 1)
            d += 1

    memo[(a, b)] = ans
    return ans

def main():
    print(count(100, 99))

main()
