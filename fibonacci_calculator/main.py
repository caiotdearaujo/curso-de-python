def fibonacci(n: int):
    if n <= 0:
        raise TypeError('The number must be greater than 0!')
    if 1 <= n <= 3:
        return n
    return fibonacci(n-1) + fibonacci(n-2)