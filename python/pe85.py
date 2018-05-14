def count(l, w):
    ans = 0
    for lp in range(1, l + 1):
        coeff = (l - lp + 1)
        row = w * (w + 1) // 2
        ans += coeff * row

    return ans

def main():
    # Consider an l x w rectangle
    # Now you want to count the number of l' x w' subrectangles
    # That value is (l - l' + 1) x (w - w' + 1)
    # This sum is over all 1 <= l' <= l

    best_dist = float('inf')
    best_area = 0
    for i in range(1, 100):
        for j in range(i, 100):
            c = count(i, j)
            dist = abs(c - 2000000)
            if dist < best_dist:
                best_dist = dist
                best_area = i * j

    print(best_dist)
    print(best_area)

main()
