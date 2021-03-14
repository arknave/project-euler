CHANGE = [1, 2, 5, 10, 20, 50, 100, 200]

# ways(n, k) = ways(n - change[k], k) + ways(n, k - 1)
def ways(n, k):
    if n < 0:
        return 0
    if n == 0 or k <= 0:
        return 1
    return ways(n - CHANGE[k], k) + ways(n, k - 1) 

def main():
    # Calculate the number of ways to make change for 200 pence.
    print ways(200, 7)

if __name__ == '__main__':
    main()
