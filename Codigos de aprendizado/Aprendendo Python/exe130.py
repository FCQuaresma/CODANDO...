'''cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('FIM')'''

'''n = 0
while n != 999:
    n = int(input('Digite um numero: '))
print('FIM')'''

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f' A soma dos valores é:  {s}')