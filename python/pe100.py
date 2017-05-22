import math

def sqrt(x):
    guess = int(math.sqrt(x))
    if guess * guess == x:
        return guess

    return None

def main():
    """
    Say we have b blue out of x total disks.
    P(BB) = b/x * (b - 1) / (x - 1) = 1/2
    2 b (b - 1) = x (x - 1)
    2 b^2 - 2 b = x^2 - x

    iterate over x and solve for b?
    """

    seed = 120
    ratio = 5.828427

    loratio = .995
    hiratio = 1.01

    bestx = 1

    while bestx <= 10**12:
        base = int(seed * ratio)
        lo, hi = int(loratio * base), int(hiratio * base)
        lo = max(lo, seed + 1)
        print('Searching in {} to {}'.format(lo, hi))

        for x in range(lo, hi):
            a = 2
            b = -2
            c = -(x * x - x)

            disc = b * b - 4 * a * c
            disc = sqrt(disc)
            if disc is None:
                continue

            num = -b + disc
            if num % (2 * a) != 0:
                continue

            root = num // (2 * a)
            bestx = x
            print(x, root)
            seed = x

            loratio += (1.0 - loratio) / 2.0
            break
        else:
            print('COULD NOT FIND!')

main()
