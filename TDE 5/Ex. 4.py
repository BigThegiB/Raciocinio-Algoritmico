'''4. Leia dois valores reais do teclado, calcular e imprimir na tela:
5. a) A soma destes valores b) O produto deles c) O quociente entre eles'''

numeros = [0,0]

numeros[0] = float(input("Insira o primeiro número"))
numeros[1] = float(input("Insira o segundo número"))

print(f"A soma entre os dois valores é {numeros[0] + numeros[1]}\nO produto entre os dois valores é {numeros[0] * numeros[1]}\nO quociente entre eles é {numeros[0]/numeros[1]} ")