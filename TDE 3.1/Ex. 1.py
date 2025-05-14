Numero = int(input('Quantos numeros serão lidos?'))
Contagem = 0
SomaTotal = 0
SomaPar = 0
SomaImpar = 0
while Contagem < Numero:
    Entrada = int(input("Insira um número"))
    SomaTotal += Entrada
    if Entrada % 2 == 0:
        SomaPar += Entrada
    else:
        SomaImpar += Entrada
    Contagem += 1

print(f"Soma Total: {SomaTotal} \nSoma Impar: {SomaImpar} \nSoma Par: {SomaPar}")
