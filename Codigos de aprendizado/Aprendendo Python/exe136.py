# PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRONICO.
'''print('=' * 30)
print('{:^30}'.format(' BANCO QUARESMA '))
print('=' * 30)
valor = int(input('Qual valor você quer sacar ? R$: '))
tot = valor
cedulas = 50
totcedulas = 0
while True:
    if tot >= cedulas:
        tot -= cedulas
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f'Total de {totcedulas} cédulas de R$ {cedulas}.')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
            totcedulas = 0
        if totcedulas == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO QUARESMA! Tenha um bom dia!')'''

#ouuuuuuuuuuuuu

print('=' * 30)
print('{:^30}'.format(' BANCO QUARESMA '))
print('=' * 30)
valor = int(input('Qual valor você quer sacar ? R$: '))
tot = valor
cedulas = 50
totcedulas = 0
while True:
    if tot >= cedulas:
        tot -= cedulas
        totcedulas += 1
    else:
        # Se houve cédulas entregues daquele valor, exibe a mensagem
        if totcedulas > 0:
            print(f'Total de {totcedulas} cédulas de R$ {cedulas}.')
        
        # Verifica se o valor restante é zero. Se sim, significa que todo o dinheiro foi sacado.
        if tot == 0:
            break # Sai do loop principal

        # Altera para a próxima cédula disponível
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        
        # Reseta o contador para a nova cédula
        totcedulas = 0
print('=' * 30)
print('Volte sempre ao BANCO QUARESMA! Tenha um bom dia!')