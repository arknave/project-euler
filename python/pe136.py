# (a + 2d)^2 - (a + d)^2 - a^2 = n
# a^2 + 4ad + 4d^2 - a^2 - 2ad - d^2 - a^2 = n
# - a^2 + 2ad + 3d^2 = n
# (3d - a) (a + d) = n
# How many values of n are there such that there is exactly one (a, d) solution to the above with positive a?
# For each value, for each a, d, 3d - a > 0 iff 3d > a, d > ceil(a/3)

CAP = 50000000
counts = [0 for _ in range(CAP)]
for a in range(1, CAP):
    for d in range((a + 2) // 3, CAP):
        v = (3 * d - a) * (a + d)

        if v > CAP:
            break

        if 0 < v < CAP:
            counts[v] += 1

print(sum(x == 1 for x in counts))
