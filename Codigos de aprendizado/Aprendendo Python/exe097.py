'''EXERCICIO ALISTAMENTO'''

from datetime import date

atual = date.today().year
nasc = int(input('Em que ano voce nasceu?: '))
idade = atual - nasc
print('Sua Idade é : {}'.format(idade))

# ler o ano de nascimento de um jovem e informar  de acordo com sua idade : se ainda vai se alistar, mostrar tempo que falta

if idade < 18:
    print(' ainda faltam {} anos para você se alistar!'.format(18 - idade))
# ler o ano de nascimento de um jovem e informar  de acordo com sua idade : se é hora de se alistar

elif idade == 18:
    print(' É seu ano de alistar-se ! pois voce tem {} anos'.format(idade))

# ler o ano de nascimento de um jovem e informar  de acordo com sua idade : ou se ja passou o tempo, mostrar o tempo que passou

else:
    print(' Seu prazo para alistar-se ja passaou faz {} anos'.format(idade - 18 ))
