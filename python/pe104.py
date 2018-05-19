def is_pandigital(s):
    return all(c in s for c in '123456789')

LAST_MASK = 1000000000

def first():
    a, b = 1, 1
    div = 1
    idx = 2
    while True:
        idx += 1
        a, b = b, a + b
        while True:
            front = b // div
            if front < int(1e9):
                break
            div *= 10
        if is_pandigital(str(front)):
            yield idx

def last():
    a, b = 1, 1
    idx = 2
    while True:
        idx += 1
        a, b = b, (a + b) % LAST_MASK
        if is_pandigital(str(b)):
            yield idx

def main():
    l_gen = last()
    f_gen = first()
    lidx, fidx = next(l_gen), next(f_gen)
    print(lidx, fidx)
    while lidx != fidx:
        if lidx < fidx:
            lidx = next(l_gen)
        else:
            fidx = next(f_gen)
        print(lidx, fidx)
main()
