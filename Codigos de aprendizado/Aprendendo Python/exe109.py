# PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS
soma = 0
cont = 0
for c in range(1, 7):
 num = int(input(f'Digite o {c}º valor : '))
 if num % 2 == 0:

# MOSTRE A SOMA APENAS DOS QUE FOREM PARES

    soma += num
    cont += 1

print( f'Voce informou {cont} numeros PARES e a a soma foi {soma} !')
