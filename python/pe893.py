import itertools

def main():
    n = 1_000_000
    sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    for x in range(10, n + 1):
        sticks.append(sum(sticks[i] for i in map(int, str(x))))

    for d in range(1, n + 1):
        for j in range(d + d, n + 1, d):
            sticks[j] = min(sticks[j], sticks[d] + sticks[j // d] + 2)

    offsets = []
    for i in range(1, n + 1):
        if i % 1000 == 0:
            print(i, len(offsets))
        for j in offsets:
            sticks[i] = min(sticks[i], sticks[i - j] + 2 + sticks[j])

        # lol, idk
        if sticks[i] <= 15:
            offsets.append(i)

    print(sum(sticks[1:]))


if __name__ == "__main__":
    main()
