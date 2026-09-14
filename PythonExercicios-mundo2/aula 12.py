nome = str(input("Qual é o seu nome?"))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Sabrina" or nome == "Maya" or nome == "Gabriel":
    print("Seu nome é belissimo!")
elif nome in "Diego Miguel giovanni":
    print("Belo nome masculino")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia {}!".format(nome))