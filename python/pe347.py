def gen_pfs(n):
    # returns a list of primes
    sieve = [[] for _ in range(n + 1)]

    for d in range(2, n + 1):
        if not sieve[d]:
            for j in range(d, n + 1, d):
                sieve[j].append(d)

    return sieve


def main():
    n = 10**7
    pfs = gen_pfs(n)
    ans = 0
    seen = set()
    for i in range(n, -1, -1):
        if len(pfs[i]) != 2:
            continue

        key = tuple(sorted(pfs[i]))
        if key not in seen:
            seen.add(key)
            ans += i

    print(ans)

if __name__ == "__main__":
    main()
