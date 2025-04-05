tarefas = []

tarefa = input('Insira uma tarefa: ')
tarefas.append(tarefa)

while tarefa != '':
    tarefa = input('Insira uma tarefa: ')
    tarefas.append(tarefa)
print(tarefas[0:-1])
