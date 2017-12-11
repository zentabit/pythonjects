
def fib(n):
    x, y, z = 0, 1, 0
    while z < n:
        z = x + y
        x = y
        y = z
        print(z)

fib(255)
