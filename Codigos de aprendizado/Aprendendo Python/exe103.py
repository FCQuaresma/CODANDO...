# jogo pedra x papel x tesoura:

titulo = ' Jogo Pedra, Papel, Tesoura! '
largura = 40
print(f"{titulo.center(largura, '=')}")

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(''' Suas opções:
      [0] pedra
      [1] papel
      [2] tesoura)''')

# jogador escolhe sua opção:

jogador  = int(input(' Qual a sua jogada? '))
print(f'JO...')
sleep(1)
print(f'KEN...')
sleep(1)
print(f'PO !')
sleep(1)

print ('=-' * 15)

# escolha computador:
print( f' Computador jogou {itens[computador]} !')

# escolha jogador:

print(f' Jogador jogou {itens[jogador]}!')
print('=-' *  15)

# condiçôes:

# computador jogo pedra

if computador == 0:
    if jogador == 0:
        print(f' EMPATE! ')
    elif jogador == 1:
        print(f' JOGADOR VENCE!')
    elif jogador == 2:
        print(f' COMPUTADOR VENCE!')
    else:
        print(f' JOGADA INVALIDA !')
              
#computador jogou papel:
    
if computador == 1:
    if jogador == 0:
        print( f' COMPUTADOR VENCE!')
    elif jogador == 1:
        print(f' EMPATE !')
    elif jogador == 2:
        print(f'  JOGADOR VENCE !')
    else:
        print(f' JOGADA INVALIDA !')

#computador jogou tesoura:

if computador == 2:
    if jogador == 0:
        print(f' JOGADOR VENCE!')
    elif jogador == 1:
        print(f' COMPUTADOR VENCE!')
    elif jogador == 2:
        print(f' EMPATE !')
    else:
        print(f' Jogada invalida!')