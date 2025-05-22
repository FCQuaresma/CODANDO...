while True:
    n = int(input(' Você quer ver a tabuada de qal valor?: '))
    if n < 0:
        break
    print('=-'*20)
    for i in range (1, 11):
        print(f' {n} X {i} = {n*i}')
    print('=-'*20)
print(' Chega de Calculos por hoje!')

# ouuuuuuuuuuuuuuuuu

'''while True:
    n = int(input('Digite um numero: '))
    print(f' Você quer ver a tabuada de qual valor?')
    print('=-'*20)
    print(f' {n} x 1 = {n*1}')
    print(f' {n} x 2 = {n*2}')
    print(f' {n} x 3 = {n*3}')
    print(f' {n} x 4 = {n*4}')
    print(f' {n} x 5 = {n*5}')
    print(f' {n} x 6 = {n*6}')
    print(f' {n} x 7 = {n*7}')
    print(f' {n} x 8 = {n*8}')
    print(f' {n} x 9 = {n*9}')
    print(f' {n} x 10 = {n*10}')
    print('=-'*20)
    if n <= 0:
        break
print(f' Chega de Calculos por hoje!')'''