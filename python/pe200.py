import heapq

CAP = 1000000
sieve = [i % 2 == 1 for i in range(CAP)]
sieve[0] = False
sieve[1] = False
sieve[2] = True
primes = [2]
for d in range(3, CAP, 2):
    if sieve[d]:
        primes.append(d)
        for j in range(d * d, CAP, 2 * d):
            sieve[j] = False

def is_prime(x):
    assert x < CAP * CAP
    for p in primes:
        if x % p == 0:
            return False
    return True

def prime_proof(x):
    s = str(x)
    n = len(s)
    for i in range(n):
        for d in range(10):
            t = s[:i] + str(d) + s[i + 1:]
            if is_prime(int(t)):
                return False
    return True

seen = set([(0, 0)])
heap = [(32, 0, 0)]
ans = []
while len(ans) < 200:
    v, a, b = heapq.heappop(heap)
    if a != b:
        # print(v, a, b)
        if "200" in str(v) and prime_proof(v):
            ans.append(v)

    if (a + 1, b) not in seen:
        seen.add((a + 1, b))
        nv = pow(primes[a + 1], 2) * pow(primes[b], 3)
        heapq.heappush(heap, (nv, a + 1, b))

    if (a, b + 1) not in seen:
        seen.add((a, b + 1))
        nv = pow(primes[a], 2) * pow(primes[b + 1], 3)
        heapq.heappush(heap, (nv, a, b + 1))

print(ans)
print(ans[-1])
