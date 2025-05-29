'''Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação'''
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

def SepararPares(MatrizOriginal):
    ListaPares = []
    ListaImpares = []
    for linha in range(len(MatrizOriginal)):
        for coluna in MatrizOriginal[linha]:
            if coluna % 2 == 0: ListaPares.append(coluna)
            else: ListaImpares.append(coluna)
    ListaCompleta = ListaPares + ListaImpares
    return ListaCompleta

def SortMatriz(MatrizOriginal,ListaCompleta):
    MatrizModificada = []
    for linha in range(len(MatrizOriginal)):
        TempColuna = []
        for coluna in range(len(MatrizOriginal[0])):
            TempColuna.append(ListaCompleta[0])
            del ListaCompleta[0]
        MatrizModificada.append(TempColuna)      
    return MatrizModificada

def PrintMatriz (Matriz, Mensagem = ""):
    print(Mensagem)
    for linha in Matriz:
        print(linha)

MatrizOriginal = CriarMatriz(15,7)
ListaCompleta = SepararPares(MatrizOriginal)
MatrizModificada = SortMatriz(MatrizOriginal,ListaCompleta)
PrintMatriz(MatrizOriginal, "Matriz Original")
PrintMatriz(MatrizModificada, "Matriz Modificada")

