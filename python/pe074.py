memo = {169: 3, 871: 2, 872: 2}
f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def factdig(n):
    return sum(f[int(x)] for x in str(n))

def size(n):
    if n in memo:
        return n

    orig = n
    seen = set([n])

    while True:
        n = factdig(n)

        if n in memo:
            memo[orig] = len(seen) + memo[n]
            return memo[orig]
        elif n in seen:
            memo[orig] = len(seen)
            return memo[orig]

        seen.add(n)

def main():
    ans = 0

    for i in range(1, 1000001):
        s = size(i)
        if s == 60:
            ans += 1

    print(ans)

main()
