import os

listed_items = []

while True:
    print("Lista de afazeres em Python")
    print("[a]dicionar  [r]emover  [l]istar")
    user_input = input("> ").lower().strip()

    match user_input:
        case "a":
            value = input("Insira valor: ")
            listed_items.append(value)
            print()
        case "r":
            while True:
                index = input("Insira o número do item: ").strip()

                if index == '':
                    break
                else:
                    try:
                        index = int(index)

                        if index < 1:
                            print("Valor não encontrado!\n")
                            break

                        listed_items.pop(index-1)
                    except TypeError:
                        print("Valor não encontrado!\n")
                    except IndexError:
                        print("Valor não encontrado!\n")
                    break
        case "l":
            if listed_items == []:
                print("Lista vazia!")
            else:
                for ind,item in enumerate(listed_items,start=1):
                    print(f"{ind}. {item}")
            print()
        case "":
            print("Programa encerrado")
            break
        case _:
            print("Insira um comando válido!")