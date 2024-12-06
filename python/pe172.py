from collections import Counter
from functools import lru_cache

@lru_cache(None)
def go(state, num_digits):
    assert all(s >= 0 for s in state)
    if num_digits == 0:
        return 1

    ans = 0
    for x in range(3):
        if state[x] > 0:
            new_state = list(state)
            new_state[x] -= 1
            new_state[x + 1] += 1
            new_state = tuple(new_state)

            ans += state[x] * go(new_state, num_digits - 1)

    return ans

def f(num_digits):
    return 9 * go((9, 1, 0, 0), num_digits - 1)

def main():
    for n in range(1, 19):
        print(n, f(n))

if __name__ == "__main__":
    main()
