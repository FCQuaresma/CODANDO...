from random import randint
from time import sleep
computador = randint(0, 5) # FAz o compuador pensar 

print('-=-' * 10)
print('Vou pensar em um numero entre 0 e 5. Tente Adivinhar...')
print('-' * 20)
jogador = int(input('Em que numero eu pensei ? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens! você conseguiu vencer !')
else:
    print('Irrullllll! você perdeu para seu comptador! eu pensei no numero {} e não no numero {}.'.format(computador, jogador))