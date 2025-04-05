'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimnto do cateto adjacente: '))

hip = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir{:.2f}'.format(hip))'''

#ouuuuuuuuuuuuuuuuu

'''import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = math.hypot(co, ca)

print(' A hipotenusa vai medir {:.2f}'.format(hip))'''

#ouuuuuuuuuuuuuuu

from math import hypot

ca = float(input('Digite o comprimento do cateto oposto: '))
co = float(input('Digite o comprimento do cateto adjacente: '))

hip = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hip))



