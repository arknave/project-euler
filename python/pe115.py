def main():
    # f(x) = number of ways of ending with black 
    # g(x) = number of ways of ending with red
    # f(x) = f(x - 1) + g(x - 1)
    # g(x) = f(x - k) for k in range(3, ...)
    m = 50
    f = [1] * (m - 1)
    g = [1] + ([0] * (m - 2))
    i = m - 1
    while f[-1] + g[-1] <= 1000000:
        f.append(f[i - 1] + g[i - 1])
        g.append(sum(f[:i - (m - 1)]))
        i += 1
    print(i - 1)

main()
