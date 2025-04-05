print('=' * 30)
print('   Analisador de traiangulos')
print('=' * 30)
a = int(input('Primeira reta? : '))
b = int(input('Segunda reta? : '))
c = int(input('Terceira reta? : '))

if a < b + c and b < a + c and c < b + a:
    print(f'Os seguimentos acima PODEM formar um triangulo!')
else:
    print(f'Os seguimentos acima NAO podem formar um triangulo!')