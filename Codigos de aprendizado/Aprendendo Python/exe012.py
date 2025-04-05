nome = ""
continuar = True
while continuar:
    nome = nome + input("Digite um nome ") + "\n]"

    x = input("Deseja continuar? Digite 'sim' ou 'não'")

    if (x.upper() == "sim"):
        continuar = True
    else:
        continuar = False

print(nome)
        
