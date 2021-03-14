def powsum(n):
    ans = 0
    while n > 0:
        d = n % 10
        ans += d ** 5
        n //= 10

    return ans

def valid(n):
    return n == powsum(n)

def main():
    ans = 0
    for i in range(10, int(1e6) + 1):
        if valid(i):
            print(i)
            ans += i

    print(ans)

main()
