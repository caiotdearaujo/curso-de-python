OPERATORS = ('+','-','*','/')

def isnumber(number):
    try:
        float(number)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


number1 = None
number2 = None
operator = None

while not isnumber(number1):
    number1 = input('Insira o primeiro número: ')

number1 = float(number1)
print()

while not isnumber(number2):
    number2 = input('Insira o segundo número: ')

number2 = float(number1)
print()

while operator not in OPERATORS:
    operator = input('Insira a operação (+ - * /): ')
    operator = operator.strip()

print()

match operator:
    case '+':
        result = number1 + number2
    case '-':
        result = number1 - number2
    case '*':
        result = number1 * number2
    case '/':
        result = number1 / number2

print(f'O resultado foi {result}')