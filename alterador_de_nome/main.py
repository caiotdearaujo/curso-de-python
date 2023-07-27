name = input('Insira seu nome: ')
new_name = ''
i = 0

if len(name) == 1:
    print('Seu nome não mudou.')
elif name:
    while i < len(name):
        if i:
            new_name += f'*{name[i]}'
        else:
            new_name += name[i]
        i += 1
    else:
        print(f'Seu novo nome é {new_name}')
else:
    print('Insira algo!')