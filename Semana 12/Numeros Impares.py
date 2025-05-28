def calcularImpar(Maximo):
    i = 0
    Impares = []
    while len(Impares) != Maximo:
        if i % 2 != 0:
            Impares.append(i)
        i += 1
    return Impares

print(calcularImpar(100))


'''def calcularImpar(maximo):
    return [2 * i + 1 for i in range(maximo)]

print(calcularImpar(100))''' #Codigo do Copilot, lembrar que numeros impares são sempre 2*i+1