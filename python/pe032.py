# find all products which can be written as a pandigital
def get_digit_counts():
    # only options are 1 4 4 or 2 3 4
    for a in range(1, 10):
        for b in range(a, 10):
            c = a + b - 1
            if a + b + c == 8:
                print(a, b, c + 1)
            if a + b + c == 9:
                print(a, b, c)

def get_digits(x):
    while x:
        yield x % 10
        x //= 10

def get_valid(a_low, a_high, b_low, b_high):
    valid = set()
    for a in range(a_low, a_high):
        for b in range(b_low, b_high):
            digits = set([0])
            pandig = True
            for x in get_digits(a):
                if x in digits:
                    pandig = False
                    break
                digits.add(x)
            if not pandig:
                continue
            for x in get_digits(b):
                if x in digits:
                    pandig = False
                    break
                digits.add(x)
            if not pandig:
                continue

            c = a * b
            for x in get_digits(c):
                if x in digits:
                    pandig = False
                    break
                digits.add(x)
            if pandig:
                print(a, b, c)
                valid.add(c)
    return valid

s = get_valid(1, 10, 1111, 10000) | get_valid(10, 100, 111, 1000)
print(sum(s))
