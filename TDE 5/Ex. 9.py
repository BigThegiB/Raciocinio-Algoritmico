'''Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.'''
Numeros = []
Posicoes = []
Contagem = 0
for i in range(10):
    Numeros.append(int(input("Insira um número: ")))
Escolhido = int(input("Número a ser procurado: "))

for i in range(len(Numeros)):
    if Numeros[i] == Escolhido:
        Posicoes.append(i)
        Contagem += 1


if Contagem == 1:
    print(f"O número {Escolhido} aparece uma vez na posição {Posicoes}")

elif Contagem > 1:
    print(f"O número aparece {Contagem} vezes nas posições {Posicoes}")

else:
    print(f"O número não aparece")


