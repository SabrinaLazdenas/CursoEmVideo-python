nome = "Sabrina"
cores = {"Limpa": "\033[m",
         "Azul":"\033[34m",
         "Amarelo":"\033[33m",
         "PretoBranco":"\033[7;30m"}

print("Olá! Muito prazer em te conhecer, {}{}{}!".format(cores["Azul"], nome,cores["Limpa"]))