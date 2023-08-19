def calculate_fatorial(n: int):
    if n < 1:
        raise IndexError(f'It\'s not possible to calculate the fatorial of {n}')

    if n == 1:
        return n
    return n * calculate_fatorial(n-1)
