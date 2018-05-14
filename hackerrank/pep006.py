def main():
    n = int(input())
    sumsq = sum(x * x for x in range(n + 1))
    sqsum = sum(range(1, n + 1)) ** 2

    print(sqsum - sumsq)

T = int(input())
for _ in range(T):
    main()
