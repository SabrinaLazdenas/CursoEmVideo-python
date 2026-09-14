distancia = float(input("Digite a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}km".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("E o preço da sua passagem será de {:.2f}".format(preco))