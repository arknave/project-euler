def main():
    single = list(range(1, 21))
    single.append(25)
    double = [2 * x for x in single]
    triple = [3 * x for x in single]
    # can't triple bulls eye
    triple.pop()
    moves = [0] + single + double + triple
    moves.sort()
    ways = [0 for _ in range(300)]
    for i in range(len(moves)):
        a = moves[i]
        for j in range(i + 1):
            b = moves[j]
            ways[a + b] += 1

    ans = 0
    for score in range(100):
        for last in double:
            if last > score:
                continue
            ans += ways[score - last]

    print(ans)

main()
