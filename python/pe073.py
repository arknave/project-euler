import math

MAXD = 12000

def brute():
    ans = 0
    for den in range(1, MAXD + 1):
        for num in range(den // 3 - 3, den // 2 + 2):
            if 2 * num < den and den < 3 * num and math.gcd(num, den) == 1:
                ans += 1

    return ans

def main():
    # Need to count the number of fractions in the range (1/3, 1/2) with
    # denominator <= MAXD

    # Easy solution: count # < 1/2, then subtract number <= 1/3
    # Must take care to only subtract coprime numbers
    # or do some inclusion exclusion bs
    # 12k is also pretty small, can just binary search for each value or brute force it

    print(brute())

main()
