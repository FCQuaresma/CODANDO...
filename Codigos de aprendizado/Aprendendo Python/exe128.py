
# Crie um programa que leia varios numeros inteiros pelo teclado

# O programa so vai parar quando digitar 999( condiçâo de parada )
num = cont = soma = 0
while num != 999:
    num = int(input(' Digite um numero inteiro [999 PARA PARAR ]: '))
    soma += num
    cont += 1
    if num == 999:
        print(' Fim do programa ')
print(f' foi digitado {cont-1} vezes e a soma entre eles é {soma-999} ')


# no final mostre quantos numeros foram digitados e qual foi a soma entre eles
