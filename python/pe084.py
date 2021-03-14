from random import randint

n = 40

def get_next(xs, x):
    ans = xs[0]
    dist = float('inf')
    for y in xs:
        d = (y + n - x) % n
        if d < dist:
            dist = d
            ans = y

    return ans

def main():
    """
    TODO: This is a dumb simulation. Setting up markov chain is non-trivial though
    """
    MOVES = 10000000
    dice_sides = 4
    freq = [0 for _ in range(n)]
    pos = 0
    doubles = 0
    cc = [2, 17, 33]
    ch = [7, 22, 36]
    cc_dest = [None, 0, 10]
    ch_dest = [None, 0, 10, 11, 24, 39, 5]
    rails = [5, 15, 25, 35]
    utils = [12, 28]
    for _ in range(MOVES):
        a, b = randint(1, dice_sides), randint(1, dice_sides)
        if a == b:
            doubles += 1
            if doubles == 3:
                pos = 10
                freq[pos] += 1
                doubles = 0
                continue
        else:
            doubles = 0

        pos = (pos + a + b) % n
        if pos in cc:
            r = randint(1, 16)
            if r < len(cc_dest):
                pos = cc_dest[r]
        elif pos in ch:
            r = randint(1, 16)
            if r < len(ch_dest):
                pos = ch_dest[r]
            elif 7 <= r <= 8:
                pos = get_next(rails, pos)
            elif r == 9:
                pos = get_next(utils, pos)
            elif r == 10:
                pos = (pos + n - 3) % n

        if pos == 30:
            pos = 10
        freq[pos] += 1

    res = [(x, i) for i, x in enumerate(freq)]
    res.sort(reverse=True)
    print(res)

main()
