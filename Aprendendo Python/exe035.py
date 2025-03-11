lojas = ['Rio de janeiro','Sao Paulo','Curitiba']

faturamento = [10000,20000,50000]


resultados = []

for i in range(3):
    tupla = (lojas[i-1],faturamento[i-1])
    resultados.append(tupla)
    
print(resultados)
