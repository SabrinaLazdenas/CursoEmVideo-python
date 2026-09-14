n1 = float(input("Primeira nota:"))
n2 = float(input("Segunda nota:"))
nota = (n1 + n2) / 2
print("Tirando {} e {}, a média do aluno é  {}".format(n1, n2, nota))
if nota >= 7:
    print("O aluno está APROVADO!")
elif nota >= 5:
    print("O aluno está em RECUPERAÇÃO!")
else:
    print("O aluno está reprovado!")