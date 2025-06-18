num = [1, 2, 3, 4]
num [1] = 9 # substitui valor
num.append(5) # adiciona valor ao final da lista
num.sort() # ordena a lista
num.sort(reverse=True) # ordena a lista de forma reversa
#num.insert(2, 0) # insere valor na posição 2
#num.pop() # remove o último valor da lista
#num.pop(2) # remove o valor na posição 2
num.insert(2, 2) # insere o valor 2 na posição 2
if 7 in num:
    print ('O número 7 está na lista')
else:
    print ('O número 7 não está na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos') # mostra o tamanho da lista / quantidade de elementos.