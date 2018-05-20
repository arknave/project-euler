def is_bouncy(x):
    s = str(x)
    has_dec, has_inc = False, False
    n = len(s)
    for i in range(1, n):
        if s[i] > s[i - 1]:
            has_inc = True
        if s[i] < s[i - 1]:
            has_dec = True

    return has_inc and has_dec

def main():
    bounce = 0
    x = 1
    while True: 
        bounce += int(is_bouncy(x))
        if 100 * bounce == 99 * x:
            print(x)
            break
        x += 1

main()
