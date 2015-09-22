def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return (fibonacci(n - 2) + fibonacci(n - 1))


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return (lucas(n - 2) + lucas(n - 1))

def sum_series(x,y,z):
