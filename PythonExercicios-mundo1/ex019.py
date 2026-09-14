from random import choice
n1 = str(input("Digite o nome de primeiro aluno:"))
n2 = str(input("Digite o nome de segundo aluno:"))
n3 = str(input("Digite o nome de terceiro aluno:"))
n4 = str(input("Digite o nome de quarto aluno:"))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))