valores = []

while True:
    entrada = input("Digite um valor (ou 's' para sair): ")
    if entrada == 's':
        break
    valores.append(float(entrada))

if valores:
    media = sum(valores) / len(valores)
    maior = max(valores)
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior}")
else:
    print("Nenhum valor foi inserido.")
