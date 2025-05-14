'''Faça um programa que leia uma quantidade indeterminada de números positivos, encerrando quando
a entrada for -1 e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-
100].'''

Continuar = True
Grupo1 = []
Grupo2 = []
Grupo3 = []
Grupo4 = []
while Continuar:
    Entrada = int(input('Insira um número: '))
    if 0 <= Entrada <= 25:
        Grupo1.append(Entrada)
    elif 26 <= Entrada <= 50:
        Grupo2.append(Entrada)
    elif 51 <= Entrada <= 75:
        Grupo3.append(Entrada)
    elif 76 <= Entrada <= 100:
        Grupo4.append(Entrada)
    elif Entrada == -1:
        Continuar = False

print(f'0-25 = {len(Grupo1)} Números\n26-50 = {len(Grupo2)} Números\n51-75 = {len(Grupo3)} Números\n76-100 = {len(Grupo4)}')