def f(n):
    for x in range(n - 2, 0, -1):
        if ((x * x) % n) == 1:
            return x

    return 1

def brute(n):
    vals = [f(x) for x in range(3, n + 1)]

    return sum(vals)

def solve(n):
    factors = [[1] for _ in range(n + 2)]
    for d in range(2, n + 2):
        for j in range(d, n + 2, d):
            factors[j].append(d)

    # factor x^2 - 1 = (x + 1) * (x - 1)
    ans = [1 for _ in range(n + 1)]
    iters = 0
    for x in range(2, n + 1):
        for a in factors[x - 1]:
            for b in factors[x + 1]:
                iters += 1
                k = a * b
                if k > n:
                    break

                if x + 1 < k:
                    ans[k] = x

    print("ITERS", iters)
    return sum(ans[3:])


def main():
    n = int(2e7)
    print(solve(n))

main()
