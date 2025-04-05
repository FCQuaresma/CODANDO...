n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = ( n1 + n2 ) / 2
print('A sua media foi {:.1f}'.format(m))
if m >= 3.0:
    print('Excelente ! Parabens !')
else:
    print('Não foi dessa vez ! estude mais')