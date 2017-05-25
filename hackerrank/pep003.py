import math

def gen_sieve(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for x in range(4, n, 2):
        sieve[x] = False
        
    for d in range(3, n, 2):
        if sieve[d]:
            for j in range(d * d, n, d):
                sieve[j] = False
    
    return sieve

def iroot(n):
    return int(math.sqrt(n))

def is_prime(sieve, n):
    if n < len(sieve):
        return sieve[n]
    
    if n % 2 == 0:
        return False
    for d in range(3, iroot(n) + 2, 2):
        if n % d == 0:
            return False
        
    return True

def solve(sieve, n):
    best = 1
    for d in range(2, iroot(n) + 2):
        if n % d == 0:
            if is_prime(sieve, d):
                best = max(best, d)
            if is_prime(sieve, n // d):
                best = max(best, n // d)
        
    return n if best == 1 else best

sieve = gen_sieve(int(1e6) + 3)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(sieve, n))
