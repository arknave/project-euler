def cross_prod(x1, y1, x2, y2):
    return (x1 * y2 - x2 * y1) >= 0

def main():
    fin = open('../data_files/p102_triangles.txt')
    ans = 0

    for line in fin:
        points = map(int, line[:-1].split(','))
        a1 = cross_prod(points[0], points[1], points[2], points[3])
        a2 = cross_prod(points[2], points[3], points[4], points[5])
        a3 = cross_prod(points[4], points[5], points[0], points[1])

        if (a1 and a2 and a3) or not (a1 or a2 or a3):
            ans += 1

    fin.close()

    print ans

if __name__ == '__main__':
    main()
