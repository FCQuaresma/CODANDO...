# PROGRAMA QUE LÊ DUAS NOTAS DE UM ALUNO E CALCULA A SUA MEDIA

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f} a media do aluno é {:.1f}'.format(n1, n2, media))
           
# MEDIA ABAIXO DE 5.0 - REPROVADO
if media < 5.0:
   print( 'sua media foi {} ! você esta REPROVADO !'.format(media))

# MEDIA ENTRE 5.0 E 6.9 - RECUPERAÇâO
elif 5.0 < media < 6.9:
   print( 'sua media foi {} ! você esta de recuperaçâo!'.format(media))
    
# MEDIA 7.0 OU SUPERIOR - APROVADO
elif media >= 7.0:
    print( ' VOCE FOIIIIII APROVADOOOO!!!... SUA MEDIA FOI {}'.format(media))