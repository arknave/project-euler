from sortedcontainers import SortedList

def gen_primes(n):
    # returns a list of primes
    sieve = list(range(n))

    primes = [2]
    for d in range(3, n, 2):
        if sieve[d] == d:
            primes.append(d)
            for j in range(d * d, n, 2 * d):
                sieve[j] = d

    return primes

def f(seq, k):
    assert k % 2 == 0

    l = k // 2
    data = SortedList(seq[:k])
    assert len(data) == k
    ans = data[l - 1] + data[l]
    for i in range(k, len(seq)):
        data.remove(seq[i - k])
        data.add(seq[i])

        assert len(data) == k
        ans += data[l - 1] + data[l]

    return ans

def main():
    primes = gen_primes(18 * 10**7)
    assert len(primes) >= 10**7
    s = [pow(p, i, 10007) for i, p in enumerate(primes, start=1)]
    s2 = [x + s[i // 10000] for i, x in enumerate(s, start=1)]

    a = SortedList(s2[:10])
    assert len(a) == 10
    m1 = a[len(a) // 2 - 1] + a[len(a) // 2]
    assert m1 == 2 * 2021.5, m1

    b = SortedList(s2[99:1000])
    assert len(b) == 901
    m2 = b[len(b) // 2]
    assert m2 == 4715.0, m2

    sub1 = f(s2[:100], 10)
    assert sub1 == 2 * 463628.5, sub1 / 2
    sub2 = f(s2[:10**5], 10**4)
    assert sub2 == 2 * 675348207.5, sub2 / 2
    ans = f(s2[:10**7], 10**5)
    print(f"{ans // 2}.{5 * (ans % 2)}")

if __name__ == '__main__':
    main()
