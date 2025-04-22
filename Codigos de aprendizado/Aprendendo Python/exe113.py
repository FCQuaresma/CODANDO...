# PROGRAMA QUE LÊ O ANO DE NASCIMENTO DE 7 PESSOAS E NO FINAL MOSTRE QUANTAS PESSOAS NÃO ATINGIRAM A MAIORIDADE E QUANTAS SÂO MAIORES.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Digite o ano a {pess}º pessoa nasceu? : '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else: 
        totmenor += 1
print(f' Ao todo tivemos {totmaior} pessoas maiores de idade !')
print(f' E também tivemos {totmenor} pessoas menores de idade !')


