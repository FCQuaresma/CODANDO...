# PROGRAMA QUE CALCULA O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMNETO.

print('{:=^40}'.format(' LOJAS FCQ '))
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('''
[1]  à vista dinheiro/cheque
[2]  à vista cartão
[3]  2 x no cartão
[4]  3 x no cartão''')

# A VISTA DINHEIRO/CHEQUE : 10% DE DESCONTO.

opcao = int(input('Qual a opção ? : '))

if opcao == 1:
    total = preco - (preco * 10 / 100)

# A VISTA NO CARTAO: 5% DE DESCONTO.

elif opcao == 2:
    total = preco - (preco * 5 / 100)

# EM ATÉ 2 X NO CARTAO : PREÇO NORMAL.

elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra de R$ {total:.2f}  vai ser parcelada em 2 X de R$ {parcela:.2f} SEM JUROS')

# 3 X OU MAIS NO CARTAO: 20% DE JUROS.

elif opcao == 4:
    total = preco + (preco * 20 / 100 )
    parcela = total / 3
    totparc = int(input(' Quantas parcelas ?'))
    parcela = total / totparc
    print(f'Sua compra de R$ {total:.2f} vai ser parcelada em {totparc} x de R$ {parcela:.2f} COM JUROS')

else:
    total = 0
    print(f'OPCAO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE !')
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')






