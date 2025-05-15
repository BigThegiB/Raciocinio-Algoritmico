'''A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido.'''

Numeros = []

for i in range (10):
    Numeros.append(int(input("Insira um número: ")))

# Pode ser percorrendo a lista com um "for i in Numeros" mas assim é mais rapido :)

Maior = max(Numeros)
Menor = min(Numeros)

print(f"O valor máximo é {Maior}\nO minímo é {Menor}\nE a amplitude é {Maior-Menor}")