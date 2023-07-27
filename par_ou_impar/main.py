"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

def isint(number):
    try:
        int(number)
    except ValueError:
        return False
    return True


number = input('Insira um número inteiro: ')

if isint(number):
    number = int(number)
    if number%2:
        print(number,'é ímpar.')
    else:
        print(number,'é par.')
elif len(number) > 0:
    print(number,'não é um número inteiro.')
else:
    print('Você não inseriu nada!')