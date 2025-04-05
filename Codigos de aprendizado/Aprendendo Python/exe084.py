velocidade = float(input('Qual a velocidade atual de um carro? '))

if velocidade > 80:
    
    print('MULTADO! Voce excedeu o limite permitido que é 80 km')
    multa = (velocidade-80) * 7
    print(' Voce deverá pagar um multa de R$: {:.2f} ! '.format(multa))
    print('Tenha um bom dia ! dirija com segurança')