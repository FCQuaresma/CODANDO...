# PROGRAMA QUE LEIA  DOIS VALORES
v1 = float(input(' Digite o primeiro valor: '))
v2 = float(input(' Digite o segundo valor: '))
# MOSTRE UM MENU
opcao = ''
while opcao != '5':
    print(''' Menu de opções:
      
      [1]SOMAR
      [2]MULTIPLICAR
      [3]MAIOR
      [4]NOVOS NUMEROS
      [5]SAIR DO PROGRAMA''')
    opcao = int(input('Escolha uma opcção: '))
    if opcao == 1:
        soma = v1 + v2
        print(f'A soma é : {soma}')
    if opcao == 2:
        mult = v1 * v2
        print(f' A multiplicação é : {mult}')
    if opcao == 3:
        if v1 > v2:
            print(f'O maior valor é {v1}')
        elif v2 > v1:
            print(f'O maior valor é {v2}')
        else:
            print('Os valores são iguais!')
    if opcao == 4:
        print('Digite novos valores: ')
        v1 = float(input(' Digite o primeiro valor: ')) 
        v2 = float(input(' Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida! Tente novamente.')
print(f'FIM DO PROGRAMA!')



    