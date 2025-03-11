qtdvalores = int(input("Digite a quantidade de números que serâo calculados"))
contador = 0
valor = 0
while contador < qtdvalores:
    valor += float(input("Digite um valor: "))
    contador +=1

media = valor/contador
print(media)
