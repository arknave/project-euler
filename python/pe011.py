fin = open('data_files/p011.txt', 'r')
parsed_input = map(lambda l: map(int, l[:-1].split()), fin.readlines())
ans = 0

#by row
for row in parsed_input:
    for x in xrange(20-4+1):
        ans = max(ans, reduce(lambda x, y: x*y, row[x:x+4]))

#by col
for col in xrange(20):
    for r in xrange(20-4+1):
        cur = 1
        for ll in xrange(4):
            cur *= parsed_input[r+ll][col]
        ans = max(ans, cur)

#by \
for row in xrange(20-4+1):
    for col in xrange(20-4+1):
        cur = 1
        for ll in xrange(4):
            cur *= parsed_input[row+ll][col+ll]
        ans = max(ans, cur)

#by /
for row in xrange(20-4+1):
    for col in xrange(4, 20):
        cur = 1
        for ll in xrange(4):
            cur *= parsed_input[row+ll][col-ll]
        ans = max(ans, cur)
print ans
