def fib():
    yield 0
    yield 1
    a, b = 1, 2
    while a <= 4000000:
        yield b
        a, b = b, a+b

print sum([x for x in fib() if x%2 == 0])
