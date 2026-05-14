matriz = [
    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4
]

for linha in range(4):
    for coluna in range(4):
        num = input(f"Digite o número da posição {linha},{coluna}: ")
        while not num.isdigit():
            num = input(f"Digite um número válido da posição {linha} {coluna}: ")
        num = int(num)
        matriz[linha][coluna] = num

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