#num = int(input('Digite um numero: '))

#print('Analisando seu numero:')
#print('unidade: {}'.format())
#print('dezena: {}'.format())
#print('centena: {}'.format())
#print('milhar: {}'.format())

#ouuuuuuuuuuuu

num = int(input('Digite um numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando seu numero:'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))