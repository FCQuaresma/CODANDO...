# Classificação do Campeonato Brasileiro

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 
         'Coritiba', 'Avai', 'Ponte Preta', 'Atlético-GO')


print(f'-+' * 30)
print(f'Lista de times Brasileirão: {times}') # mostra a lista
print(f'-+' * 30)
print(f'Os 5 primeiros colocados sâo: {times[0:5]}') # mostra os 5 primeiros
print(f'-+' * 30)
print(f' Os 4 ultimos colocados sâo: {times[-4:]}')# mostra os 4 ultimos
print(f'-+' * 30)
print(f'Times em ordem alfabetica: {sorted(times)}')# mostra os times em ordem alfabetica
print(f'-+' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')# mostra a posiçao do Chapecoense

#sorted = classificado
#index = posiçao, indice
