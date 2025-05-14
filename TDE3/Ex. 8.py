'''
Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
qual o valor da soma e da média aritmética do conjunto.
'''
NumeroCount = 1
NumeroStorage = 0
while NumeroCount <= 10:
    NumeroInput = int(input(f'Insira um número, {NumeroCount}/10 '))
    NumeroStorage += NumeroInput
    NumeroCount += 1
print('A soma de todos os números é:', NumeroStorage,'E a média é', NumeroStorage/10)