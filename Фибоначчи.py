while True:
    fib = lambda n: 0 if n < 1 else 1 if n == 1 else fib(n - 1) + fib(n - 2)
    x = int(input('x='))
    n = 0
    while x > fib(n): n += 1
    print('fibonacci number' if fib(n) == x else 'other number')
