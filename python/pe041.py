import itertools

# we know 4 has a pandigital prime
# candidates are 5, 6, 7, 8, 9
# just try them one at a time and break if not possible
# well.... 1+2+3+4+5 = 15, all divisible by 3
# +6, 21, same with 6
# +7, 28, so we start at 7
# +8, 36, skip 8
# +9, 45 so 7 is the only answer

# there's only 7! = 5040 permutations, so trial division should be fast enough

def is_prime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    for d in range(3, x, 2):
        if x % d == 0:
            return False
        if d * d > x:
            break

    return True

ans = 0
for perm in itertools.permutations(range(1, 8)):
    x = int(''.join(str(y) for y in perm))
    if is_prime(x):
        ans = max(ans, x)

print(ans)
