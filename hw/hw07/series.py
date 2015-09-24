def fibonacci(n):
    """
    Returns the nth number from the Fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return (fibonacci(n - 2) + fibonacci(n - 1))


def lucas(n):
    """
    Returns the nth number in the Lucas sequence
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return (lucas(n - 2) + lucas(n - 1))


def sum_series(n, y=0, z=1):
    """
    Returns the nth number in a sequence starting with
    y and z
    """
    if y == 0 and z == 1:
        return fibonacci(n)
    elif y == 2 and z == 1:
        return lucas(n)
    else:
        if n == 0:
            return y
        elif n == 1:
            return z
        else:
            return (sum_series(n - 2, y, z) + sum_series(n - 1, y, z))
