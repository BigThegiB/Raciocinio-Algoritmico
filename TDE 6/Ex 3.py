'''Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados.'''

import random
def CheckMatriz(MatrizChecada,Numero):
    for Linhas in MatrizChecada:
        if Numero in Linhas:
            return True
    return False


def CriarMatriz(Linhas,Colunas):
    Matriz = []
    RandomNumber = 0
    for linha in range(Linhas):
        TempColunas = []
        for coluna in range(Colunas):
            while True:
                RandomNumber = random.randint(100,999) #Não sei se era para incluir o 100 e o 999 na conta, se não era finge que eu botei 101 e 998
                if not CheckMatriz(Matriz,RandomNumber) and RandomNumber not in TempColunas:
                    TempColunas.append(RandomNumber)
                    break
        Matriz.append(TempColunas)

    return Matriz

def MaiorElemento(MatrizChecada):
    MaiorLinha = 0
    MaiorNumero = 0
    for linha in range(len(MatrizChecada)):
        for coluna in MatrizChecada[linha]:
            if coluna > MaiorNumero:
                MaiorNumero = coluna
                MaiorLinha = linha
    return MaiorLinha

def MenorElemento(MatrizChecada,LinhaChecada):
    MenorNumero = (MatrizChecada[LinhaChecada][0])
    for coluna in MatrizChecada[LinhaChecada]:
        MenorNumero = coluna if coluna < MenorNumero else MenorNumero
    return MenorNumero

def PrintMatriz (Matriz, Mensagem = ""):
    print(Mensagem)
    for linha in Matriz:
        print(linha)

Matriz = CriarMatriz(4,4)
MaiorLinha = MaiorElemento(Matriz)
PrintMatriz(Matriz, "Matriz criada: ")
print(f"A linha com o maior elemento é a  {MaiorLinha+1}ª linha, e o menor elemento dela é {MenorElemento(Matriz,MaiorLinha)}")

