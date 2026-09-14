from random import randint
v = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I]")).strip().upper()[0]
    print(f"você jogou {jogador} e o computador {computador}, total de {total}", end=" ")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu!")
            v += 1
            print("Vamos jogar novamente...")
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceu!")
            v += 1
            print("Vamos jogar novamente...")
        else:
            print("Você perdeu!")
            break
print(f"GAME OVER! Você venceu {v} vezes.")

