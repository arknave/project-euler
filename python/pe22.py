fin = open("../data_files/p022_names.txt", "r")
names = map(lambda x: x[1:-1], fin.readlines()[0].split(","))
fin.close()

names.sort()

def score(name):
    ans = 0
    for c in name:
        ans += ord(c)-ord('A')+1
    return ans

summ = 0
for i, name in enumerate(names):
    summ += (i+1)*score(name)
print summ
