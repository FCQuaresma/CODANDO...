cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: # Este é o loop principal que mantém o programa rodando
    while True: # Este loop interno garante que o número digitado seja válido
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
            break # Se o número for válido, sai deste loop interno
        print('Tente novamente. ', end='') # Se não for válido, pede de novo

    print(f'Você digitou o numero {cont[num]}') # Mostra o número por extenso 

    resp = '' # Inicializa a resposta para o próximo loop de validação
    while resp not in 'SN': # Este loop garante que a resposta seja 'S' ou 'N'
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N': # Se a resposta for 'N', sai do loop principal, encerrando o programa
        break
print('Fim do programa! Volte sempre!')

