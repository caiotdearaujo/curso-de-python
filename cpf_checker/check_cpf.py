import re

def check_cpf(cpf: str | int):
    if type(cpf) is int:
        cpf = str(cpf)
    
    cpf = re.sub(
        r'[^0-9]',
        '',
        cpf
    )

    if cpf == cpf[0]*len(cpf):
        return False

    nine_digits = ''
    for i in cpf:
        if i.isdecimal():
            nine_digits += i
        
        if len(nine_digits) == 9:
            break

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

    generated_end = digit1 + digit2
    VALID_REQUIREMENT = generated_end == cpf[-2:]
    
    if VALID_REQUIREMENT:
        return True
    return False    