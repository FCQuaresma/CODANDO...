ListaNomes = []

while True :
    nome = input("Digite seu nome:")
    ListaNomes.append(nome)

    continuar = input("Deseja continuar? Digite sim ou nao ")
    if(continuar==" nao" or continuar== "NAO"):
        break
    print(ListaNomes)
