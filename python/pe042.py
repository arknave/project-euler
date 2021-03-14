# 26 * 15 = 390, sqrt ~ 20. Let's do 30 to be safe
tri = [x * (x + 1) // 2 for x in range(1, 30)]

def score(word):
    return sum(ord(c) - ord('A') + 1 for c in word)

def main():
    fin = open('../data_files/p042_words.txt')
    words = [word.strip('"') for word in fin.readline().strip().split(',')]
    ans = sum(score(word) in tri for word in words)
    print(ans)

if __name__ == '__main__':
    main()
