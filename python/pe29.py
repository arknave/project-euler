def main():
    cap = 100
    s = set(a**b for a in range(2, cap + 1) for b in range(2, cap + 1))
    print(len(s))

main()
