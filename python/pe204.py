# Count the number of values <= 10^9 that have no prime factors greater than 100

import heapq

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    return all(x % d > 0 for d in range(3, min(10, x), 2))

primes = [x for x in range(2, 101) if is_prime(x)]
# primes = [2, 3, 5]

n = 10**9

vis = set([1])
pq = [1]
while pq:
    x = heapq.heappop(pq)
    for p in primes:
        v = p * x
        if v <= n and v not in vis:
            heapq.heappush(pq, v)
            vis.add(v)

print(len(vis))

