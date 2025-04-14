# PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE:

from datetime import date

atual = date.today().year
ano = int(input(' Qual ano do seu nascimento? '))
idade = atual - ano
print(f'Você nasceu em {ano} e tem {idade} anos !!')

# ATE 9 ANO: MIRIM

if idade <= 9:
    print(f'Você é Mirim ! pois tem {idade} anos!')

# ATE 14 ANOS: INFANTIL

elif idade <= 14:
    print(f'Você é INFANTIL ! pois tem {idade} anos!')

# ATE 19 ANOS: JUNIOR

elif idade <= 19:
    print(f'Você é JUNIOR ! pois tem {idade} anos!')

# ATE 25 ANOS: SENIOR

elif idade <= 25:
    print(f'Você é SENIOR ! pois tem {idade} anos!')

# ACIMA: MASTER

else:
    print(f'Você é MASTER ! pois tem {idade} anos!')

    