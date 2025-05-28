'''Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.'''

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

def MaiorNaColuna(TempMatriz):
    Maiores = []
    for Linha in range(len(TempMatriz)):
        Maior = 0
        for Coluna in TempMatriz[Linha]:
            if Coluna > Maior:
                Maior = Coluna
        Maiores.append(Maior)
    return Maiores

def MediaVetor(Vetor):
    return sum(Vetor)/len(Vetor)

Matriz = CriarMatriz(4,4)
print("Matriz: ")
for i in Matriz:
    print(i)

print(f"Vetor dos maiores números: {MaiorNaColuna(Matriz)}\nMédia do vetor:{MediaVetor(MaiorNaColuna(Matriz))}") #Para um codigo mais otimizado, definir o Maiores antes
