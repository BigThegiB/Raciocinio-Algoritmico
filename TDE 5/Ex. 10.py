'''Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLidoTemp.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLidoTemp, e vImpares
contendo somente os números ímpares de vLidoTemp. Os vetores vPares e vLidoTemp não deverão conter
zeros. Mostre então os três vetores'''

vLido = []

for i in range(10):
    num = int(input("Insira um número: "))
    if "0" not in str(num):
        vLido.append(num)

vPares = [Num for Num in vLido if Num % 2 == 0]
vImpares = [Num for Num in vLido if Num % 2 != 0]
print(f"Lidos: {vLido}\nPares: {vPares}\nImpares: {vImpares}")