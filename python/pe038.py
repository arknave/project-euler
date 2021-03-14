def pandigital(x):
    prod_string = str(x)
    i = 2
    while len(prod_string) < 9:
        prod_string += str(i * x)
        i += 1
    if ''.join(sorted(prod_string)) == "123456789":
        return prod_string
    else:
        return None

def main():
    best_prod = "918273645"
    ranges = (x for y in (range(91, 100), range(911, 1000), range(9111, 10000)) for x in y)
    for i in ranges:
        prod_string = pandigital(i)
        if prod_string is not None:
            best_prod = max(best_prod, prod_string)
    print best_prod

if __name__ == '__main__':
    main()
