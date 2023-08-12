import random
from check_cpf import *

def generate_cpf(formatted: bool):
    nine_digits = ''
    for _ in range(9):
        nine_digits += str(random.randint(0,9))

    multiplier1 = 10
    product1 = 0
    for i in nine_digits:
        i = int(i)
        product1 += i * multiplier1
        multiplier1 -= 1

    module1 = product1 * 10 % 11

    digit1 = str(module1) if module1 <= 9 else '0'

    ten_digits = nine_digits + digit1

    multiplier2 = 11
    product2 = 0
    for i in ten_digits:
        i = int(i)
        product2 += i * multiplier2
        multiplier2 -= 1

    module2 = product2 * 10 % 11

    digit2 = str(module2) if module2 <= 9 else '0'

    cpf = ten_digits + digit2

    validation = check_cpf(cpf)
    
    if not validation:
        print('INVALID GENERATION ERROR')
        return None

    if not formatted:
        return cpf

    first_part = ''
    second_part = ''
    third_part = ''
    fourth_part = ''

    for index, item in enumerate(cpf):
        if 0 <= index <= 2:
            first_part += item
        elif 3 <= index <= 5:
            second_part += item
        elif 6 <= index <= 8:
            third_part += item
        elif 9 <= index <= 10:
            fourth_part += item

    cpf = '.'.join((first_part, second_part, third_part))
    cpf = '-'.join((cpf, fourth_part))

    return cpf