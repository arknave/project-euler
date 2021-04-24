import math

def brute():
    n, k = "123", 678910
    v, e = 2, 1

    last = 0
    while k:
        v *= 2
        e += 1
        if str(v).startswith(n):
            print(e, e - last)
            assert last == 0 or (e - last) in [196, 289, 485]
            last = e
            k -= 1

    print(e)


def take1():
    opts = [(e, 2**e) for e in (196, 289, 485)]
    n, k = "123", 678910
    v, e = float(pow(2, 90)), 90

    while k:
        print(e, k)
        k -= 1
        for ee, x in opts:
            vx = v * x
            if str(int(10000.0 * vx)).startswith(n):
                e += ee
                v = vx
                break
        else:
            assert False

    print(e)


def main():
    # 12 * 10^k < 2^n < 13 * 10^k
    # log 12 + k < n log(2) < log 13 + k
    lg2 = math.log10(2)
    
    lg123, lg124 = math.log10(123), math.log10(124)
    k = 678910
    n = 89
    while k > 0:
        n += 1
        if lg123 - 2.0 <= n * lg2 % 1 <= lg124 - 2.0:
            k -= 1

    print(n)

if __name__ == "__main__":
    main()
