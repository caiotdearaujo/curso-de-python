print('Algoritmo contador de quantidade de aparições em Python')
print('Observação: não há distinguição entre maiúsculas e minúsculas, mas há entre acentuadas e não acentuadas.')
print()

sentence = input('Insira uma frase:\n> ')
sentence = sentence.lower().strip()

already_analized_letters = []
most_appeared_quantity = 0
most_appeared_letter = ''
i = 0

while i < len(sentence):
    current_letter = sentence[i]

    if current_letter == ' ':
        i+=1
        continue

    if current_letter in already_analized_letters:
        i+=1
        continue

    current_appeared_quantity = sentence.count(current_letter)

    if current_appeared_quantity > most_appeared_quantity:
        most_appeared_quantity = current_appeared_quantity
        most_appeared_letter = current_letter
    
    i+=1

if most_appeared_letter:
    print(f'A letra que mais apareceu foi "{most_appeared_letter}".')
    print(f'Ela apareceu {most_appeared_quantity} vezes.')