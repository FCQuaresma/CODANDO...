# Ler o primeiro termo de uma PA e sua razao, e mostr os 10 primeiros termos.

primeiro = int(input('primeiro termo: '))
r = int(input('razâo: '))

termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} -> ',end='')
        termo += r
        c += 1

    print('PAUSA')

    mais = int(input('Quantos termos voce quer mostrar a mais ? ' ))
print(f'Progressao finalizada com {total} termos mostrados')
