# PROGRAMA QUE LEIA O PRIMEIRO TERMO  E A RAZAO DE UMA P.A 

primeiro = int(input('Digite o primeiro termo da P.A : '))
razao = int(input(' Digite a razão da P.A: '))
decimo = primeiro + (10 - 1) * razao

# NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA P.A.

for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end = ' -> ')
print('ACABOU')
    
   
