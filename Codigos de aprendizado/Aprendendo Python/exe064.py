d = int(input('Quantos dias foi alugado ?:R$'))
km = float(input('Quantos kilometros rodou?:R$'))

p = (d * 60) + (0.15*km)

print('O total a pagar é de : R$ {}'.format(p))

