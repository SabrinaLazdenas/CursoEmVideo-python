s = cont = 0
while True:
    n = int(input("Digide um valor: (999 para parar):"))
    if n == 999:
        break
    cont += 1
    s += n
print(f"A soma dos {cont} valores é {s}!")