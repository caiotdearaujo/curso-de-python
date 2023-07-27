def create_multiplication(multiplicator):
    def multiplicate(n):
        return n * multiplicator
    return multiplicate

duplicar = create_multiplication(2)
triplicar = create_multiplication(3)
quadruplicar = create_multiplication(4)

print(duplicar(2))