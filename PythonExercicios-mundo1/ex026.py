frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes em uma frase".format(frase.count('A')))
print("A primeira letra A apareceu na pocição {}".format(frase.find("A")+1))
print("A ultima letra A apareceu na pocição {}".format(frase.rfind("A")+1))