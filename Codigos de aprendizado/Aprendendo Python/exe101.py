# Calculando Indice de Massa Corporal

peso = float(input('Qual o seu peso ? :' ))
altura = float(input('Qual a sua altura ?: '))
               
imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo de peso')
elif imc < 24.9:
    print('Peso normal')
elif imc < 29.9:
    print('Sobrespeso')
elif imc < 39.9:
    print('Obesidade')
else:
    print('Obesidade mórbida')
