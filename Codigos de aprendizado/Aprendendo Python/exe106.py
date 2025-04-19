# PROGRAMA QUE ME MOSTRE TODOS OS NUMEROS PARES ENTRE 1 e 50:
from time import sleep

for cont in range(0, 51, 2):
    sleep(0.25)
    print(cont, end = ' ')
    
print( 'FIm')