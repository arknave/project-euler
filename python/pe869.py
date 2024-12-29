from fractions import Fraction as Q

import pelib


class Trie:
    def __init__(self):
        self.data = [[None, None]]
        self.freq = [0]

    def add(self, x):
        cur = 0
        self.freq[cur] += 1
        while x:
            b = x & 1
            x >>= 1
            if self.data[cur][b] is None:
                node = len(self.data)
                self.data.append([None, None])
                self.freq.append(0)
                self.data[cur][b] = node

            cur = self.data[cur][b]
            self.freq[cur] += 1

    def solve(self, node):
        """
        Expected score given you start at node N and are not done.
        """
        lhs, rhs = self.data[node]
        ans = 0.0
        if lhs is None and rhs is None:
            ans = 0.0
        elif lhs is None:
            p = self.freq[rhs] / self.freq[node]
            ans = p * (1.0 + self.solve(rhs))
        elif rhs is None:
            p = self.freq[lhs] / self.freq[node]
            ans = p * (1.0 + self.solve(lhs))
        else:
            lhs_prob = self.freq[lhs] / self.freq[node]
            rhs_prob = self.freq[rhs] / self.freq[node]

            base = lhs_prob * self.solve(lhs) + rhs_prob * self.solve(rhs)
            ans = base + max(lhs_prob, rhs_prob)

        return ans


def solve(n):
    primes = pelib.gen_primes(n)
    print("Generated primes")
    trie = Trie()
    for p in primes:
        trie.add(p)

    print("Created trie")
    return trie.solve(0)


def main():
    for n in [10, 30, 10**8]:
        print(n, solve(n))


if __name__ == "__main__":
    main()
