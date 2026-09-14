velocidade = float(input("Qual é a velocidade atual do carro?"))
if velocidade > 80:
    print("MULTADO! Você exedeu o limite permitido de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Você deve uma multa de {:.2f}".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança!")