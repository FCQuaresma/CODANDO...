contador = 0
soma_notas = 0

while contador < 6:
    nota = float(input("Digite a nota do aluno:"))
    soma_notas += nota
    contador +=1 

media = soma_notas/contador

print(" A média de notas é", media)
