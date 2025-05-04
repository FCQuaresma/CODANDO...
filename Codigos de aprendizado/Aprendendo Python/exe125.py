# Ler o primeiro termo de uma PA e sua razao, e mostr os 10 primeiros termos.

primeiro = int(input('primeiro termo: '))
r = int(input('razâo: '))

termo = primeiro
c = 1

while c <= 10:
    print(f'{termo} -> ',end='')
    termo += r
    c += 1
print('FIM')