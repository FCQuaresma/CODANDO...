tot = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input(' Nome do produto: '))
    preco = float(input(' Preço do produto: R$ '))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input(' Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM'))
print(f'O total da compra foi R$ {tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')