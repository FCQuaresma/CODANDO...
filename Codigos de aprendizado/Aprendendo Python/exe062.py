salario = float(input('Qual o salário do funcionário/ R$ '))

#novo = salario*1.15

#ouu

#novo = salario*15/100

#ouuuuu

novo = salario + (15/100*salario)

print('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a ganhar R$: {:.2f}'.format(salario, novo))
