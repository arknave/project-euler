def is_pal(s):
    if s[0] == '0':
        return False
    return s == s[::-1]

def my_bin(s):
    return bin(int(s))[2:]

ans = 0
for j in range(10):
    if is_pal(str(j)) and is_pal(my_bin(str(j))):
        ans += j

for i in range(1000):
    s = str(i) + str(i)[::-1]
    if is_pal(s) and is_pal(my_bin(s)):
        ans += int(s)

    if i < 100:
        for j in range(10):
            s = str(i) + str(j) + str(i)[::-1]
            if is_pal(s) and is_pal(my_bin(s)):
                ans += int(s)

print(ans)
