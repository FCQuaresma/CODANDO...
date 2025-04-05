salario = float(input('Qual o seu salario ? R$ : '))

if salario > 1250:
    print(f'Seu novo salario é : R$ {salario * 1.10:.2f}')
else:
    print(f'Seu novo salario é: R$ {salario * 1.15:.2f}')