# A frase é um PALINDROMO?
# strip() = tira os espaços.
# upper() = deixa tudo em maiusculo.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # split() = separa as palavras.
junto = ''.join(palavras)
print(f' Você digitou a frase: {junto}') 
inverso = ''
# len() = conta o tamanho da string
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f' o inverso de {junto} é {inverso}')
print(f'{junto, inverso}')
if inverso == junto:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um PALÍNDROMO!')
