from collections import defaultdict
import itertools

def dedupe(s):
    out = []
    for c in s:
        if not out or c != out[-1]:
            out.append(c)

    return ''.join(out)

def do_map(mapping, value):
    return ''.join(mapping[c] for c in value)

def main():
    with open('../data_files/p098_words.txt') as fin:
        words = [word[1:-1] for word in fin.read().strip().split(',')]
    grouped = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        grouped[key].append(word)

    squares = set(x * x for x in range(int(1e6)))
    anagrams = {k: v for k, v in grouped.items() if len(v) > 1}

    ans = 0

    for key, values in anagrams.items():
        simple = dedupe(key)
        digits = '0123456789'
        num_chars = len(simple)
        for perm in itertools.permutations(digits, num_chars):
            mapping = dict(zip(simple, perm))
            translated = [do_map(mapping, value) for value in values]
            if any(x[0] == '0' for x in translated):
                continue
            translated = [int(x) for x in translated]
            if all(x in squares for x in translated):
                ans = max(ans, max(translated))

        print('Processed', key)

    print(ans)

main()

# 18769
