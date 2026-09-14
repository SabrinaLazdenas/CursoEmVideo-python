from datetime import date
totmaior =0
totmenor =0
atual = date.today().year
for p in range(1,8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(p)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
       totmenor += 1
print("Ao todo foram {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))
