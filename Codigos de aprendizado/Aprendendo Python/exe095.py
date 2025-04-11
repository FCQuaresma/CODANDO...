num = int(input('Digite um numero qualquer:'))
print('''escolha uma das bases para conversão:
      [1] converter para binario]
      [2] converter para octal
      [3] converter para hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {} '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opcao ==3:
    print('{} convertido para HEXADECIMAL é ogual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida! Tente Novamente!')