tot18 = totH = totmulher20 = 0
while True:
    idade = int(input(' Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ').strip().upper()[0])
        if idade >= 18:
             tot18 += 1
        if sexo == 'M':
             totH += 1
        if sexo == 'F' and idade < 20:
             totmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input(' Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totmulher20}')
