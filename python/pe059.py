blacklist = [chr(x) for x in range(0x20)] + ['#', '$', '*', '+', '~', '{', '}', '|', '`']

def weird(code):
    return chr(code) in blacklist

def encode(inp, a, b, c):
    l = [a, b, c]
    out = []
    p = 0
    for byte in inp:
        code = byte ^ l[p]
        if weird(code):
            return (None,)

        out.append(code)
        p += 1
        p %= 3

    return (''.join(map(chr, out)), sum(out))

def main():
    fin = open('../data_files/p059_cipher.txt')
    inp = map(int, fin.readline().rstrip().split(','))
    fin.close()

    start = ord('a')
    end = ord('z') + 1
    for a in xrange(start, end):
        for b in xrange(start, end):
            for c in xrange(start, end):
                ans = encode(inp, a, b, c)
                if ans[0] is not None:
                    print ans

if __name__ == '__main__':
    main()
