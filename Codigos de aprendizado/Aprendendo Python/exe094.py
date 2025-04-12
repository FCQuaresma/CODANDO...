vcasa = float(input('Qual valor da casa ? R$: '))
sal = float(input('Qual salario do comprador? R$: '))
financ = int(input('Quantos anos de financiamento? R$: '))

prestacao = vcasa / (financ * 12)
minimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestaçao sera de R$ : {:.2f}'.format(vcasa, financ, prestacao ))

#print('COMPARANDO tem que oaga {} e o minimo é {} '.format(prestacao, minimo))

if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo nao pode ser CONCEDIDO!')