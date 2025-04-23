# PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

# NO FINAL DO PROGRAMA , MOSTRAR:

for i in range(1, 5):
    print('=-' * 20)
    print(f'CADASTRO DA {i} º PESSOA')
    print('=-' * 20)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade # NOME DO HOMEM MAIS VELHO
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20: # QUANTAS MULHERES TEM MENOS DE 20 ANOS
        totmulher20 += 1
mediaidade = somaidade / 4 # A MEDIA DE IDADE DO GRUPO

print(f' A media de idade do grupo é de {mediaidade:.2f} anos')
print(f'O homem mais velho é {nomevelho} com {maioridadehomem} anos')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')



