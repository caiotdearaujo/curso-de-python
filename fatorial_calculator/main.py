def calculate_factorial(n: int):
    if n <= 1:
        return 1
    return n * calculate_fatorial(n-1)