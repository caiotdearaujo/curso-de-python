def isnumber(value):
    try:
        float(value)
    except ValueError: 
        return False
    return True


valor1 = input("Insira o primeiro valor: ")
valor2 = input("Insira o segundo valor: ")

if isnumber(valor1) and isnumber(valor2):
    valor1 = float(valor1)
    valor2 = float(valor2)

if valor1 > valor2:
    print(f'{valor1=} é maior que {valor2=}')
elif valor2 > valor1:
    print(f'{valor2=} é maior que {valor1=}')
elif valor1 == valor2:
    print(f'{valor1=} é igual a {valor2=}')