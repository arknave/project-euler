import math

def count_geo(n):
    # Consider a sequence a < b < c
    # say factor is x / y where x > y
    # Then c must have a square divisor
    is_prime = [True for _ in range(n + 2)]
    is_prime[0] = is_prime[1] = False
    for d in range(2, n + 2):
        if is_prime[d]:
            for j in range(d * d, n + 2, d):
                is_prime[j] = False

    ans = 0
    for y in range(1, n):
        y2 = y * y
        for a in range(y2, n, y2):
            if not is_prime[a - 1]:
                continue

            for x in range(y + 1, n):
                if math.gcd(x, y) != 1:
                    continue
                b = a // y * x
                c = b // y * x
                if c > n:
                    break
                if is_prime[b - 1] and is_prime[c - 1]:
                    ans += a + b + c - 3
    
    return ans

def main():
    for n in [100, 10**8]:
        print(n, count_geo(n))


if __name__ == "__main__":
    main()
