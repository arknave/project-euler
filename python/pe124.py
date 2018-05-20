def main():
    cap = 100000
    rad = [1 for _ in range(cap + 1)]
    for d in range(2, cap + 1):
        if rad[d] == 1:
            for j in range(d, cap + 1, d):
                rad[j] *= d
    inds = list(range(cap + 1))
    inds.sort(key=lambda x: (rad[x], x))

    # print(rad)
    print(inds[10000])

main()
