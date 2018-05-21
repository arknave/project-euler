def main():
    # f(x) = number of ways of ending with black 
    # g(x) = number of ways of ending with red
    # f(x) = f(x - 1) + g(x - 1)
    # g(x) = f(x - k) for k in range(3, ...)
    f = [1, 1]
    g = [1, 0]
    for i in range(2, 51):
        f.append(f[i - 1] + g[i - 1])
        g.append(sum(f[:i - 2]))
    print(f[50] + g[50])

main()
