from functools import reduce

f = open('../data_files/p008.txt')
instr = ''.join(f.readlines())
instr = instr.replace('\n', '')
ans = 0
for i in range(0, len(instr)):
    ans = max(ans, reduce(lambda x, y: x * y, map(int, instr[i:i + 13])))

print(ans)
