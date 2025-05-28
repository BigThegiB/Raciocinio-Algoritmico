"""
Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.
Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
de A por k. Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij
"""

def UserInput(Texto = ""):
    while True:
        try:
            return int(input(Texto))
        except ValueError:
            print("Insira um número")

def CriarMatriz(Linhas,Colunas):
    Matriz = []
    Count = 1
    for linha in range(Linhas):
        TempColunas = []
        for coluna in range(Colunas):
            TempColunas.append(UserInput(f"Entre com o {Count}° número"))
            Count += 1
        Matriz.append(TempColunas)
    return Matriz

def MultiplicarMatrix(Matriz,Multi):
    MatrizMultiplicada = []
    for Linhas in range(len(Matriz)):
        MatrizMultiplicada.append([Matriz[Linhas][Elemento] * Multi for Elemento in range(len(Matriz[0]))]) 
    return MatrizMultiplicada

MatrizOriginal = CriarMatriz(3,3)
Multi = UserInput("Por qual valor deseja multiplicar a matriz? ")
MatrizMultiplicada = MultiplicarMatrix(MatrizOriginal,Multi)
print("Matriz Original")
for linha in MatrizOriginal:
    print(linha)
print(f"Matriz Multiplicada por {Multi}")
for linha in MatrizMultiplicada:
    print(linha)
