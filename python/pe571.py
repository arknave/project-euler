import itertools

def is_pan(x, base):
    seen = [False for _ in range(base)]
    while x:
        seen[x % base] = True
        x //= base

    return all(seen)

def solve(b):
    ans = 0
    count = 0
    for p in itertools.permutations(range(b)):
        if p[0] == 0:
            continue
        x = 0
        for y in p:
            x = b * x + y

        if all(is_pan(x, base) for base in range(b - 1, 1, -1)):
            print(x)
            ans += x
            count += 1
            if count == 10:
                break

    return ans

def main():
    print(solve(10))
    print(solve(12))

if __name__ == "__main__":
    main()
