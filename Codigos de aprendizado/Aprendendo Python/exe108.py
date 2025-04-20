# refazendo uma tabuada, porém utilizando a estrutura de laço "for"
mult = 0
num =int(input(' Digite um numero para ver sua tabuada : '))
print('-=' * 20)
for c in range(1, 11):
 mult = mult + num
 print(f' {num} x {c} = {mult}')

 #ouuuuu

'''num =int(input(' Digite um numero para ver sua tabuada : '))
for c in range(1, 11):
 print(f'{num} X {c} = {num*c}') '''
