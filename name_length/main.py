"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('Qual o seu primeiro nome? ')
name = name.strip()

if name:
    if len(name) <= 4:
        print('Seu nome é curto!')
    elif 5 <= len(name) <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Você não inseriu nada!')