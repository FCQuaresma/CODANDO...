'''import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Tercero Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print('O aluno escolhido foi : {}'.format(escolhido))'''

#ouuuuuuuuuuuuu

from random import choice

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Tercero Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi : {}'.format(escolhido))
