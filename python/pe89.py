table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
def value(s):
    n = len(s)
    res = 0
    for i, c in enumerate(s):
        if i + 1 < n and table[s[i + 1]] > table[c]:
            res -= table[c]
        else:
            res += table[c]

    return res

def write_dig(out, dig, ten, five, one):
    if dig == 9:
        out.append(one)
        out.append(ten)
        return
    elif dig >= 5:
        out.append(five)
        dig -= 5

    if dig == 4:
        out.append(one)
        out.append(five)
        dig = 0

    for _ in range(dig):
        out.append(one)

def write(x):
    thousands = x // 1000
    out = []
    for _ in range(thousands):
        out.append('M')

    x -= 1000 * thousands

    hundreds = x // 100
    write_dig(out, hundreds, 'M', 'D', 'C')
    x -= 100 * hundreds

    tens = x // 10
    write_dig(out, tens, 'C', 'L', 'X')
    x -= 10 * tens

    write_dig(out, x, 'X', 'V', 'I')
    return ''.join(out)

def main():
    ans = 0
    with open('../data_files/p089_roman.txt', 'r') as fin:
        for line in fin:
            line = line.strip()
            v = value(line)
            w = write(v)
            print('{} -> {} -> {}'.format(line, v, w))
            assert(len(w) <= len(line))
            ans += len(line) - len(w)

    print(ans)

main()
