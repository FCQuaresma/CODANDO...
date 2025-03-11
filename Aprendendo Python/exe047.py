#file = open('abc.txt', 'w+')
#file.write('linha 1\n')
#file.write('linha 2\n')
#file.write('linha 3\n')

#file.seek(0, 0)
#print('Lendo Linhas:')
#print(file.read())
#print('#############')

#file.seek(0, 0)
#print(file.readline(), end='')
#print(file.readline(), end='')
#print(file.readline(), end='')

#file.seek(0, 0)
#for linha in file.readlines():
#    print(linha, end='')

#file.close()

with open('abc.txt','a+') as file:
    file.write('outra linha\n')
    file.seek(0)
    print(file.read)



