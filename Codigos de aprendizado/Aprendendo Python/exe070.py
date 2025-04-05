'''import math

a = float(input('Digite o angulo que você deseja: '))

sen=math.sin(math.radians(a))
cos=math.cos(math.radians(a))
tg=math.tan(math.radians(a))

print('O angulo de {} tem o SEN de {:.2f}'.format(a, sen))
print('O angulo de {} tem o COS de {:.2f}'.format(a, cos))
print('O angulo de {} tem a TANG de {:.2f}'.format(a, tg))'''

#ouuuuuuuuuuuuuuuu

from math import radians, sin, cos, tan

an = float(input('Digite o angulo que você deseja:'))

seno = sin(radians(an))
print('O angulo de {} tem SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo de {} vale COSSENO de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O angulo de {} vale TNAGNETE de {:.2f}'.format(an, tangente))

