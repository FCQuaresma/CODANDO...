frase = str(input('Digite uma frase: ')).upper().strip()

print(' a letra A aparece {} vezes na frase'.format(frase.count('A')))
print(' a primeira letra aparceu na posiçâo {} '.format(frase.find('A')+1))
print(' A ultima letra A apareceu na posiçao {}'.format(frase.rfind('A')+1))