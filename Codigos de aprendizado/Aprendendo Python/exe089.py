a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

# verificando quem é o menor 

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando quem é o maior

maior = a

if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c

print('O menor valor digitado foi : {}'.format(menor))
print('O maior valor digitado foi : {}'.format(maior))