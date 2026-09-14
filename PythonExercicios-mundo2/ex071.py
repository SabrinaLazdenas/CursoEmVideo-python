print("=" * 30)
print("{:^30}".format("Banco Sabrina"))
print("=" * 30)
valor = int(input("Qual o valor você quer sacar? R$"))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f"Total de {totcedula} cédulas de R$ {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print("Volte sempre!")
