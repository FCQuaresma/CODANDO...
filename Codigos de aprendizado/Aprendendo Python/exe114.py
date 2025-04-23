# PROGRAMA QUE LEIA O PESO DE 5 PESSOAS.
'''maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}º pessoa (Kg):  '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    
# NO FINAL MOSTRE O MAIOR E O MENOR PESO LIDOS.

print(f' o maior peso lido foi {maior} Kg')
print(f' O menor peso lido foi {menor} kg')'''

maior = None
menor = None

for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}º pessoa (Kg):  '))
    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso

print(f' O maior peso lido foi {maior} Kg')
print(f' O menor peso lido foi {menor} kg')