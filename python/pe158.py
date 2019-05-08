choose = [[1 for _ in range(30)] for _ in range(30)]
for i in range(30):
    for j in range(1, i):
        choose[i][j] = choose[i - 1][j - 1] + choose[i - 1][j]

def p(n):
    ans = choose[26][n]
    # set of letters to pick
    # now for each bitmask substring
    # order the 0s descending, then the 1s descending
    # valid if and only if the largest 1 is greater than the smallest 0
    # means every bitstring is valid except
    # 000, 001, 011, 111
    # cba, cba, cba, cba
    return choose[26][n] * ((1 << n) - (n + 1))

def main():
    print(max(p(n) for n in range(1, 27)))

main()
