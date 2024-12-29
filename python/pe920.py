import math

def compute_tau(n):
    tau = [1]*(n + 1)
    tau[0] = 0
    for d in range(2, n + 1):
        for j in range(d, n + 1, d):
            tau[j] += 1

    return tau


def brute(n):
    tau = compute_tau(n)
    seen = set()
    ans = 0
    for x, t in enumerate(tau):
        if t > 0 and x % t == 0 and t not in seen:
            seen.add(t)
            ans += x

    return ans


def brute_tau_values(primes, idx, max_exp, n, val = 1):
    if n == 0:
        return []

    if n == 1 or idx == len(primes):
        return [val]

    ans = []
    cur = n
    for i in range(max_exp + 1):
        if cur == 0:
            break

        ans += brute_tau_values(primes, idx + 1, i, cur, val * (i + 1))
        cur //= primes[idx]

    return ans


def divisors(x):
    for d in range(1, x + 1):
        if d * d > x:
            break

        if x % d == 0:
            yield d
            if d * d != x:
                yield x // d


def solve(n):
    primes = [p for p, t in enumerate(compute_tau(100)) if t == 2]
    # TODO: tune
    primes = primes[:40]
    assert math.prod(primes) > n

    p2 = int(math.log(n) / math.log(2))
    tau_values = brute_tau_values(primes, 0, p2 + 1, n)
    tau_values = sorted(set(tau_values))

    def factor(x):
        res = []
        for p in primes:
            e = 0
            while x % p == 0:
                e += 1
                x //= p
            if e > 0:
                res.append((p, e))

        return res

    def search(req, x, used):
        if x == 1:
            return n + 1 if req else 1

        ans = n + 1
        for d in divisors(x):
            if d == 1:
                continue

            if req and d <= req[0][1]:
                continue

            if req:
                p = req[0][0]
                assert p in primes
                ans = min(ans, pow(p, d - 1) * search(req[1:], x // d, used + [p]))
            else:
                for p in primes:
                    if p in used:
                        continue
                    ans = min(ans, pow(p, d - 1) * search([], x // d, used + [p]))
                    break
                else:
                    assert False, (req, x, used)

        return ans

    def m(tau):
        req = factor(tau)

        return search(req, tau, [])

    ans = 0
    for tau in tau_values:
        mt = m(tau)
        if mt <= n:
            assert mt % tau == 0
            ans += mt

    return ans

def main():
    print(solve(10**3))
    print(solve(10**16))

if __name__ == "__main__":
    main()
