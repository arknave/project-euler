moves = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def solve(x, y, z):
    s = set((a, b, c) for a in range(x) for b in range(y) for c in range(z))
    d = 10
    f = [0 for _ in range(d)]
    for a in range(-d, x + d + 1):
        for b in range(-d, y + d + 1):
            for c in range(-d, z + d + 1):
                dist = min(abs(a - aa) + abs(b - bb) + abs(c - cc) for aa, bb, cc in s)
                if dist < d:
                    f[dist] += 1
    return f[1:]

def main():
    # each iteration introduces some new set of cubes that appear in all future ones
    # first: 1 dist away 2*(xy + xz + yz) = 2 * (2 + 3 + 6) = 2 * 11 = 22
    # second: 2 dist away: first + 4 * (x + y + z) = 22 + 4 * (1 + 2 + 3) = 22 + 24 = 46
    # third: 3 dist away??? first + second + third = 78, so third = 32
    # how tf does one get 32...
    # fourth gap is 40

    # 22, 46, 78, 118
    # 24, 32, 40
    # 8, 8, 8

    # v0 = 2 * (xy + xz + yz) - xyz
    # v(n) = v0 + 8n

    # p0 = xyz
    # p(n) = p0 + v0 + v1 + ... + vn
    # p(n) = p0 + n v0 + 4 * n * (n - 1)

    # print(solve(4, 8, 30))

    guess = 1000000
    goal = 1000
    freq = [0 for _ in range(guess + 1)]
    for x in range(1, guess + 1):
        for y in range(x, guess + 1):
            if x * y > guess:
                break
            for z in range(y, guess + 1):
                if x * y * z > guess:
                    break

                p0 = 2 * (x * y + x * z + y * z)
                v0 = 4 * (x + y + z)
                i = 0
                while True:
                    p = p0 + i * v0 + 4 * i * (i - 1)
                    if p > guess:
                        break
                    # print(x, y, z, i, p)
                    freq[p] += 1
                    i += 1

    for i in range(guess + 1):
        if freq[i] == goal:
            print(i)
            break

main()
