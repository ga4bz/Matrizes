matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = (input(f"Digite um valor para [{i}][{j}]: "))
        while not valor.isdigit():
            valor = (input(f"Digite um valor válido para [{i}][{j}]: "))
        valor = int(valor)
        linha.append(valor)
    matriz.append(linha)

for linha in range(4):
    print(matriz[linha])

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"O maior valor é {maior} e ele está na linha {linha_maior} na coluna {coluna_maior}")