MEMO_CAP = 900
memo = {1: False, 89: True}

def sqdigit(n):
    ans = 0
    while n > 0:
        d = n % 10
        ans += d * d
        n //= 10

    return ans

def ends_eighty_nine(n):
    if n < MEMO_CAP and n in memo:
        return memo[n]

    stack = [n]
    while stack[-1] not in memo:
        stack.append(sqdigit(stack[-1]))

    ans = memo[stack[-1]]
    for x in stack:
        if x < MEMO_CAP:
            memo[x] = ans

    return ans

def main():
    ans = 0

    for i in range(1, 10000001):
        if i % 1000000 == 0:
            print(i)
        if ends_eighty_nine(i):
            ans += 1

    print(ans)

main()
