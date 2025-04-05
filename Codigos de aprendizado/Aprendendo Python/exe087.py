#Esse foi meu codigo antes de ver a correção do exercicio:

'''distancia = float(input('Qual a distancia da sua viagem ?'))
print('Voce esta prestes a comecar uma viagem de {} kilometros'.format(distancia))

normal = 0.50 * distancia
promocional = 0.45 * distancia

if distancia <= 200:
    print( 'o preço da sua passagem é: {}'.format(normal))
else:
    print('sua passagem promocional é: {}'.format(promocional))'''

# agora vendo a correção:

'''distancia = float(input('Qua a distância da sua viagem ? '))
print('Você esta prestes a começar uma viagem de {} kilometros'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem sera de R$: {:.2f} reais '.format(preco))'''

# ou de outra forma :

distancia = float(input('Qua a distância da sua viagem ? '))
print('Você esta prestes a começar uma viagem de {} kilometros'.format(distancia))
preco = distancia * 0.50 if  distancia  <= 200 else distancia * 0.45
print('E o preço da sua passagem sera de R$ {:.2f}'.format(preco))