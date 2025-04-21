# leia um numero inteiro e diga ou não se ele é numero primo.

num = int(input('Digite um numero: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print(f'\033[36m',end=' ')
    else:
        print(f'\033[31m',end = ' ')
    print(f'{c}', end=' ')
print(f'O numero {num} foi divisivel {tot} vezes !')
if tot == 2:
    print(f' O numero {num} é primo !')
else:
    print(f' O numero {num} não é primo !')
