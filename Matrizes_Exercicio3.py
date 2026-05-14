alunos_info = [
    [10231, 8, 9, 0],
    [10458, 7, 10, 0],
    [10792, 5, 7, 0],
    [11046, 9, 10, 0],
    [11387, 6, 7, 0]
]

maior = 0
matricula_maior = 0

for linha in range(5):
    alunos_info[linha][3] = (alunos_info[linha][1] + alunos_info[linha][2]) / 2
    if alunos_info[linha][3] > maior:
        maior = alunos_info[linha][3]
        matricula_maior = alunos_info[linha][0]

print(f"Maior Nota: {maior}\nMatrícula do aluno: {matricula_maior}")