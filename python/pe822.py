import heapq

MOD = 1234567891
def s_slow(n, m):
    heap = [(x, i) for i, x in enumerate(range(2, n + 1))]

    a = [0 for _ in heap]
    heapq.heapify(heap)
    for _ in range(m):
        x, i = heapq.heappop(heap)
        a[i] += 1
        heapq.heappush(heap, (x * x, i))

    return sum(x for x, i in heap) % MOD

def s_fast(n, m):
    heap = [x for x in range(2, n + 1)]
    while m > 0 and heap[0] < n:
        m -= 1
        x = heapq.heappop(heap)
        heapq.heappush(heap, x * x)

    heap.sort()
    each = m // len(heap)
    bonus = m % len(heap)

    ans = 0
    for i, x in enumerate(heap):
        times = each + int(i < bonus)
        ans += pow(x, pow(2, times, MOD - 1), MOD)
        ans %= MOD

    return ans


def main():
    print(s_slow(5, 3))
    print(s_fast(5, 3))
    print(s_slow(10, 100))
    print(s_fast(10, 100))
    print(s_fast(10**4, 10**16))

if __name__ == "__main__":
    main()
