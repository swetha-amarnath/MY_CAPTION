#fibonacci series for n=15, n=5

def fib(n):
    x = 0
    y = 1
    if n == 1:
        print(x)
    else:
        print(x)
        print(y)
        for i in range(2,n):
            z = x + y
            x = y
            y = z
            print(z)
fib(15)

fib(5)