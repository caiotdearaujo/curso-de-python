"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

def check_time(time: int):
    time = int(time)
    NOON = [i for i in range(12)]
    AFTERNOON = [i+12 for i in range(6)]
    NIGHT = [i+18 for i in range(6)]

    if time in NOON:
        print('Bom dia!')
    elif time in AFTERNOON:
        print('Boa tarde!')
    elif time in NIGHT:
        print('Boa noite!')
    else:
        print('Insira um horário válido.')


DIV = ('h',':',' ')
time = input('Que horas são? ')
time = time.strip()

if len(time) > 0 and time[0].isdigit():
    if len(time) > 1 and time[1].isdigit():
        if len(time) > 2 and time[2] in DIV:
            check_time(time[0:2])
        else:
            print('Insira um horário válido.')
    else:
        check_time(time[0])
else:
    print('Insira um horário válido.')