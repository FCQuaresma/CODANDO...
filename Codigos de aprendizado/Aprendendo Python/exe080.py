n = str(input('Digite seu nome: ')).strip()

nome = n.split()

print('Muito prazer em te conhecer ! seu primeiro nome é {}'.format(nome))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))