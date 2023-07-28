from questions import *

for question in questions:
    print(question.get("Pergunta"))

    for key, value in enumerate(question.get("Opções")):
        print(key_format.get(key), value)

    guess = input("Insira a letra de sua resposta: ").lower().strip()

    if question.get("Resposta") == guess:
        print("Você acertou!")
    else:
        print("Errrou!")
    print()