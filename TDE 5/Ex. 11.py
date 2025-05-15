'''Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
depois, os números impares. Mostre o vetor antes de depois da modificação.'''
#Tentar começar a user funções

def InputPositivo(Texto = ""):
    while True:
        try:
            num = int(input(Texto))
            if num >= 0:
                return num
            print("Apenas números positivos são aceitos")
        except ValueError:
            print("Insira um número")

Inicial = []

for i in range(10):
    num = InputPositivo("Insira um número positivo: ")
    Inicial.append(num)

Sorted = [Num for Num in Inicial if Num % 2 == 0]
Sorted += [Num for Num in Inicial if Num % 2 != 0]

print(f"Lista Inicial: {Inicial}\nLista Organizada: {Sorted}")