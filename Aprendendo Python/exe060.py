n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))

area = n1*n2
l = area/2

print('Sua parede tem dimensao de {}x{} e sua area é de {} m2'.format(n1, n2, area ))
print('Para pintar essa parede, você precisara de {}l de tinta'.format(l))