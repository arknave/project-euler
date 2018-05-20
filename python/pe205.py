def gen(d, v, cc, s = 0):
    if v == 0:
        cc[s] += 1
    else:
        for i in range(1, d + 1):
            gen(d, v - 1, cc, s + i)

def main():
    p, c = [0 for _ in range(37)], [0 for _ in range(37)]
    gen(4, 9, p)
    gen(6, 6, c)

    pden = sum(p)
    cden = sum(c)

    ans = 0
    for w in range(1, 37):
        ans += p[w] * sum(c[:w])

    print(ans, pden * cden)
    print('{:.7f}'.format(ans / (pden * cden)))

main()
