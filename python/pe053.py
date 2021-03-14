def build_triangle(n):
    resp = [[1], [1, 1]]
    for i in xrange(2, n + 1):
        row = [1]
        for j in xrange(1, i):
            row.append(resp[-1][j - 1] + resp[-1][j])
        row.append(1)
        resp.append(row)
    return resp

def main():
    resp = build_triangle(100)
    flat = [elem for sublist in resp for elem in sublist]
    print len(filter(lambda x: x > 1000000, flat))

if __name__ == '__main__':
    main()
