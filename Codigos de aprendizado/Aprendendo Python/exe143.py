listagem = ('banana', 'maçã', 'laranja', 'uva', 'manga', 
            'abacaxi', 'kiwi', 'morango', 'cereja', 'pera', )

for palavra in listagem:
    print(f'\n Na palavra {palavra.upper()} temos', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

   