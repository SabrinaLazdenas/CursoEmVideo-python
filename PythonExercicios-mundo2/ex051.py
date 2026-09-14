print("="*25)
print("10 TERMOS DE UMA PA")
print("="*25)
n = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = n + (10 - 1) * razao
for c in range(n, decimo + razao, razao):
    print("{} ".format(c), end=" ⮕ ")
print("ACABOU!")