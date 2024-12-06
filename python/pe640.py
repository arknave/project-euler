def main():
    # A state is: cards, dice state
    CARDS = 12
    DIE_SIDES = 6
    DIE_STATES = DIE_SIDES * DIE_SIDES + 1
    num_states = (1 << CARDS) * DIE_STATES

    def idx(mask, die):
        return mask * DIE_STATES + die;

    def split(state):
        return state // DIE_STATES, state % DIE_STATES

    dp = [105.0 for _ in range(num_states)]
    dp[idx(0, DIE_STATES - 1)] = 0.0

    while True:
        changed = False

        for state in range(num_states):
            if dp[state] == 0.0:
                continue

            mask, die = split(state)
            if die == DIE_STATES - 1:
                ev = sum(dp[idx(mask, d)] for d in range(DIE_STATES - 1)) / (DIE_STATES - 1)
                ev += 1.0
                if ev != dp[state]:
                    dp[state] = ev
                    changed = True
            else:
                a, b = divmod(die, DIE_SIDES)
                for x in [a, b, a + b + 1]:
                    ev = dp[idx(mask ^ (1 << x), DIE_STATES - 1)]
                    if ev < dp[state]:
                        dp[state] = ev
                        changed = True

        if not changed:
            break

    print(dp[idx((1 << CARDS) - 1, DIE_STATES - 1)])

if __name__ == "__main__":
    main()
