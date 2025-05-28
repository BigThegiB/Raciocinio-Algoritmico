'''Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores:'''
import random
def CriarMatriz(Linhas,Colunas):
    Matriz = []
    RandomNumber = 0
    for linha in range(Linhas):
        TempColunas = []
        for coluna in range(Colunas):
            RandomNumber = random.randint(10,99) 
            TempColunas.append(RandomNumber)
        Matriz.append(TempColunas)

    return Matriz

Figura = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

def SeparacaoFigura(Matriz,Figura):
    MatrizSeparada = []
    for linha in range(len(Matriz)):
        SeparadaTemp = []
        for coluna in range(len(Matriz[0])):
            if Figura[linha][coluna] == 1:
                SeparadaTemp.append(Matriz[linha][coluna])
            else: SeparadaTemp.append(0)
        MatrizSeparada.append(SeparadaTemp)
    return MatrizSeparada

def SomaFigura(MatrizSeparada):
    sum = 0
    for linha in range(len(MatrizSeparada)):
        for coluna in MatrizSeparada[linha]:
            sum += coluna
    return sum

def PrintMatriz (Matriz, Mensagem = ""):
    print(Mensagem)
    for linha in Matriz:
        print(linha)

def Replace0s(MatrizCom0):
    for linha in range(len(MatrizCom0)):
        for coluna in range(len(MatrizCom0[0])):
            if MatrizCom0[linha][coluna] == 0:
                MatrizCom0[linha][coluna] = ''
    return MatrizCom0

Matriz = CriarMatriz(5,5)
MatrizSeparada = SeparacaoFigura(Matriz,Figura)
Soma = SomaFigura(MatrizSeparada)
MatrizArrumada = Replace0s(MatrizSeparada)

PrintMatriz(Matriz,"Matriz Original: ")
PrintMatriz(MatrizArrumada,"Matriz Seguindo a figura: ") 
print(f"Soma da Matriz Separada: {Soma}")