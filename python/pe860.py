import functools
import itertools
import math

MOD = 989898989

def combo(facts, seq):
    tot = sum(seq)
    ans = 1
    for x in seq:
        ans *= facts[tot]
        ans %= MOD
        ans *= pow(facts[x] * facts[tot - x], MOD - 2, MOD) % MOD
        ans %= MOD
        tot -= x

    return ans


@functools.cache
def can_win(state):
    res = False
    if state[0]:
        res |= not can_win((state[1], state[0] - 1, state[3], state[2]))
    if state[2]:
        res |= not can_win((state[1], state[0], state[3], state[2] - 1))
    if state[3]:
        res |= not can_win((state[1] + 1, state[0], state[3] - 1, state[2]))

    return res

def can_win_fast(state):
    k = min(state[2:])
    gold_moves = 2 * state[0] + (state[2] - k) + (state[3] + 1 - k) // 2
    silver_moves = 2 * state[1] + (state[3] - k) + (state[2] - k) // 2

    return gold_moves > silver_moves

n = 9898
facts = [1]
for i in range(1, n + 1):
    facts.append(i * facts[-1] % MOD)

ans = 0
for delta in range(-(n // 2), n // 2 + 1):
    # x, x + delta, y + 4 * delta, y
    # 2x + 5 * delta + 2y = n
    d = n - 5 * delta
    if d % 2 != 0 or d < 0:
        continue

    for x in range(d // 2 + 1):
        y = (d - x - x) // 2
        if x + delta >= 0 and y + 4 * delta >= 0:
            ans += combo(facts, (x, x + delta, y + 4 * delta, y))
            ans %= MOD

print(ans)
