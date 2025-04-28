from random import randint
computador = randint(0, 10)
print(f'Sou seu computador... Pensei em um numero entre 0 e 10. ')
print(f'Sera que voce consegue adivinhar ? ')
acertou = False
palpites = 0
while not acertou:
    jogador =  int(input('Qual o seu palpite ? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print(f'Parabens! Voce acertou com {palpites} tentativas. ')