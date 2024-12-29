from collections import deque

class MaxQueue:
    def __init__(self):
        self.data = deque([])
        self.peaks = deque([])

    def append(self, x):
        self.data.append(x)

        while self.peaks and x > self.peaks[-1]:
            self.peaks.pop()
        self.peaks.append(x)

    def popleft(self):
        x = self.data.popleft()
        if self.peaks[0] == x:
            self.peaks.popleft()

    def get_max(self):
        return self.peaks[0]


def main():
    n, k = 100_000_000, 100_000
    divs = [0 for _ in range(n + 1)]
    for x in range(1, n + 1):
        for y in range(x, n + 1, x):
            divs[y] += 1

    q = MaxQueue()
    for i in range(1, k + 1):
        q.append(divs[i])

    ans = q.get_max()
    for i in range(k + 1, n + 1):
        q.popleft()
        q.append(divs[i])
        ans += q.get_max()

    print(ans)

if __name__ == "__main__":
    main()
