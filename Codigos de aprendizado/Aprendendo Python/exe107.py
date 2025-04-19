# PROGRAMA QUE CALCULA A SOMA ENRTRE TODOS OS NUMEROS IMPARES  QUE SAO MULTIPLOS DE 3 E QUE SE ENCONTREM NO INTERVALO  DE 1 ATE 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
   if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de {cont} valores solicitados é igual a : {soma}')