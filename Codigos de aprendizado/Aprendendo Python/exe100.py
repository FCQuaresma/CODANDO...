# Desafio dos TRIANGULOS

'''L1 = int(input('Digite o primeiro lado: '))
L2 = int(input('Digite o segundo lado: '))
L3 = int(input('Digite o terceiro lado: '))

print (f'Um lado mede: {L1} cm, o segundo lado mede: {L2} cm, e o terceiro lado mede : {L3} cm')

# Equilatero : todos os lados são iguais

if L1 == L2 == L3:
    print('Seu triangulo é equilatero! pois, todos os lados são iguais! ')

# Isosceles : dois lados iguais

elif L1 == L2 or L1 == L3 or L3 == L2:
    print('Seu triangulo é equilatero! pois, tem dois lados com a mesma medida!')

# Escaleno:todos os lados diferenetes.

else:
    print('Seu triangulo é escaleno ! pois, todos os lados possuem medidades diferentes !')'''

#ouuuuuuuuuuuuu

L1 = float(input('Digite o primeiro lado: '))
L2 = float(input('Digite o segundo lado: '))
L3 = float(input('Digite o terceiro lado: '))

print('A condiçâo de existência de um triângulo é : A soma de dois lados deve ser maior que o terceiro lado!')

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print (' Os segmentos acima PODEM FORMAR UM TRIANGULO, pois preenchem a condiçâo de existencia!',end='')
    if L1 == L2 == L3:
        print('EQUILATERO!')
    if L1 != L2 != L3 != L1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print(' Os segmentos acima NÂO PODEM FORMAR UM TRIANGULO, pois nâo preenchem a condiçâo de existencia!')


