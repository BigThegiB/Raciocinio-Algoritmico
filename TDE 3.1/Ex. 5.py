'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5 x 4
x 3 x 2 x 1 = 120'''

Entrada = int(input('Insira um número inteiro: '))
Soma = Entrada
for Fator in range(Entrada-1, 0, -1):
    Soma = Soma * Fator


print(f"{Entrada}! é igual à {Soma}")