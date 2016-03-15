def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b) #printing fibonacci
        yield b #generator mode
        a,b = b, a+b
        n = n + 1
    return 'done'