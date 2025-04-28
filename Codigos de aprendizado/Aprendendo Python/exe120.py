# COMPUTADOR PENSA EM UM NUMERO ENTRE 0 E 10.
from random import randint

computador = randint(0, 10)

tentativas = 0


# JOGADOR TENTARÁ ADIVINHAR ATÉ ACERTAR



while True:
    jogador = int(input('Sou seu computador !...Pensei em um número entre 0 e 10. Tente adivinhar: '))
    if jogador < computador:
        print('mais...tente novmente')
        tentativas += 1
    
    elif jogador > computador:
        print('menos...tente novamente')
        tentativas += 1
        
    else:
        print('Parabens! Você acertou !')
        print('Você tentou {} vezes'.format(tentativas)) # MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER

