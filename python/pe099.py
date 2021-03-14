from math import log

def main():
    fin = open('../data_files/p099_base_exp.txt')
    data = []
    for i, line in enumerate(fin):
        a, b = map(int, line.strip().split(','))
        data.append((b * log(a), i + 1))

    data.sort()
    print(data[-5:])


main()
