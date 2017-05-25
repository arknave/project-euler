import bisect

def is_pal(n):
    return str(n) == str(n)[::-1]

def main():
    base = int(1e5)
    pals = [i * j for i in range(100, 1000) for j in range(i + 1, 1000) if is_pal(i * j) and (i * j) > base]
    pals.sort()

    t = int(input())
    for _ in range(t):
        n = int(input())
        i = bisect.bisect_left(pals, n)
        print(pals[i - 1])

main()
