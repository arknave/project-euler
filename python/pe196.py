from math import sqrt

def gen_primes(n):
    sieve = [True for _ in range(n)]
    primes = [2]
    for d in range(3, n, 2):
        if sieve[d]:
            primes.append(d)
            for j in range(d, n, d):
                sieve[j] = False
    return primes

def seg_sieve(start, end):
    sz = end - start + 1
    is_prime = [True for _ in range(sz)]
    primes = gen_primes(int(sqrt(end)) + 2)
    for prime in primes:
        p_start = ((start + prime - 1) // prime) * prime
        if p_start <= prime:
            p_start = 2 * prime

        for x in range(p_start, end + 1, prime):
            is_prime[x - start] = False

    return is_prime

def row(n):
    start = n * (n - 1) // 2
    return list(range(start + 1, start + n + 1))

def S(n):
    lines = [row(n + d) for d in range(-2, 3)]
    start = lines[0][0]
    end = lines[-1][-1]
    sieve = seg_sieve(start, end)
    print('done seg sieve')
    grid = [[sieve[x - start] for x in line] for line in lines]
    is_core = [[False for x in line] for line in lines]
    for i, line in enumerate(grid):
        for j, v in enumerate(line):
            found = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy and dy == 0:
                        continue
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[nx]) and grid[nx][ny]:
                        found += 1
            is_core[i][j] = grid[i][j] and found >= 2
    print('done core')

    # print('\n'.join(str(g) for g in grid))
    #print('\n'.join(str(g) for g in is_core))

    ans = 0
    for i, x in enumerate(lines[2]):
        if not grid[2][i]:
            continue
        valid = is_core[2][i]
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = 2 + dx, i + dy
                if 0 <= ny < len(lines[nx]) and is_core[nx][ny]:
                    valid = True
                    break
        if valid and grid[2][i]:
            # print(x)
            ans += x

    return ans

def main():
    print(8, S(8))
    print(9, S(9))
    print(S(5678027) + S(7208785))

main()
