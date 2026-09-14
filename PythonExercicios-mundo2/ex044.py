print("{:=^40}".format(" LOJAS SABRINA "))
compras = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO: 
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á  vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no crtão""")
opcao = int(input("Sua opção?:"))
if opcao == 1:
    total = compras - (compras * 10 / 100)
elif opcao == 2:
    total = compras - (compras * 5 / 100)
elif opcao == 3:
    total = compras
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!".format(parcela))
elif opcao == 4:
    total = compras + (compras * 20 / 100)
    totparcela = int(input("Quantos parcelas?"))
    parcela = total / totparcela
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS!".format(totparcela, parcela))
else:
    total = 0
    print("OPÇÃO INVALIDA!.Tente novamente.")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(compras, total))