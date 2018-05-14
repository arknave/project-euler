from collections import deque

def search(s, v):
    """Find largest x such that 20 * s * x + x^2 <= v"""
    # -20s + sqrt(400 s + 4v) / 2
    for x in range(1, 10):
        if (20 * s + x) * x > v:
            return x - 1

    return 9

def sqrt(n):
    """Yield the digits of sqrt(n) in order"""
    state = 0
    digs = deque(str(n))
    val = int(digs[0])
    digs.popleft()
    if len(digs) % 2 == 1:
        val = 10 * val + int(digs[0])
        digs.popleft()

    while True:
        # Find the largest x such that (20 * state * x + x^2 <= val)
        x = search(state, val)
        yield x
        val = val - ((20 * state + x) * x)
        state = 10 * state + x
        val *= 100
        if digs:
            val += 10 * int(digs[0])
            digs.popleft()
            val += int(digs[0])
            digs.popleft()

def main():
    ans = 0
    squares = [x * x for x in range(12)]
    for x in range(2, 101):
        if x in squares:
            continue

        gen = sqrt(x)
        out = []
        for _ in range(100):
            dig = next(gen)
            out.append(dig)
            ans += dig

    print(ans)
    
main()
