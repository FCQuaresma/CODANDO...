# A frase é um PALINDROMO?
# strip() = tira os espaços.
# upper() = deixa tudo em maiusculo.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # split() = separa as palavras.
junto = ''.join(palavras)
print(f' Você digitou a frase: {junto}') 