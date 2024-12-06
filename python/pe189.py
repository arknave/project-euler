from collections import defaultdict
from functools import cache

def color_up(downs):
    if not downs:
        return {(x,): 1 for x in range(3)}

    res = defaultdict(int)
    for state, freq in downs.items():
        k = len(state)
        cur = []
        def inner(idx):
            if len(cur) == k + 1:
                res[tuple(cur)] += freq
                return

            for x in range(3):
                valid = (idx == 0 or x != state[idx - 1]) and (idx == k or x != state[idx])
                if valid:
                    cur.append(x)
                    inner(idx + 1)
                    cur.pop()

        inner(0)

    return res

def color_down(ups):
    res = defaultdict(int)

    res = defaultdict(int)
    for state, freq in ups.items():
        k = len(state)
        cur = []
        def inner(idx):
            if len(cur) == k:
                res[tuple(cur)] += freq
                return

            for x in range(3):
                valid = x != state[idx]
                if valid:
                    cur.append(x)
                    inner(idx + 1)
                    cur.pop()

        inner(0)

    return res


ups = color_up({})
for _ in range(7):
    downs = color_down(ups)
    ups = color_up(downs)

ans = sum(ups.values())

print(ans)
