nome = input('Insira seu nome: ')
altura = float(input('Insira a sua altura (em metros): '))
peso = float(input('Insira seu peso (em quilogramas): '))
IMC = peso/altura**2

print(f'Seu nome é {nome}, sua altura é {altura}m, seu peso é {peso}kg, logo seu IMC é {IMC:.2f}')