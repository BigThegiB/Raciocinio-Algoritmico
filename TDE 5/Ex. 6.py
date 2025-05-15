'''Ler 4 números inteiros e calcular a soma dos que forem par.'''
Numeros = [0,0,0,0]
Pares = []
Soma = 0
for i in range (4):
    Numeros[i] = int(input("Insira um número"))
    if Numeros[i] % 2 == 0:
        Pares.append(Numeros[i])
for i in Pares:
    Soma += i

print(f"A soma é {Soma}")

