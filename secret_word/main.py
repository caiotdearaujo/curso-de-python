import random

WORDS = ['cacador','assustador','irmandade','otorrinolaringologista','musiquinha']
word = random.choice(WORDS)

tries = 0
inserted_letters = []

correct_guesses = 0
guessed_letters = {
    i: '_' for i in range(len(word))
}

while True:
    if tries:
        print(f'Tentativas: {tries}')

    if inserted_letters != []:
        print('Letras já inseridas:',end=' ')
        for index, item in enumerate(inserted_letters):
            end = '\n' if index == len(inserted_letters) - 1 else ', '
            print(item,end=end)

    for index, item in guessed_letters.items():
        end = '\n' if index == len(guessed_letters) - 1 else ''
        print(item, end=end)
    
    guess = input('Insira uma letra: ').strip().lower()

    if (len(guess) == 1) and (guess.isalpha()) and (guess not in inserted_letters):
        for index,item in enumerate(word):
            if guess == item:
                guessed_letters[index] = item
                correct_guesses += 1
            
        tries += 1
        inserted_letters.append(guess)

        if correct_guesses == len(word):
            break
    elif len(guess) != 1 or not guess.isalpha():
        print('Insira apenas letras!')
    elif guess in inserted_letters:
        print('Letra já inserida!')
    
    print()

print(f'\nParabéns, a palavra era {word}!')
print(f'Você acertou em {tries} tentativas.')