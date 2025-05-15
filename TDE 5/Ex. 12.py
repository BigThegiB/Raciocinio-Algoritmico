'''Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
usuário (sem repetição) e indique quantos acertos ele teve.'''
import random
def Apostas(): #Só pra testar mais função :)
    Resultado = []
    for i in range(6):
        while True:
            num = random.randint(1,60)
            if num not in Resultado:
                Resultado.append(num)
                break
    return Resultado
def UserInput(Texto = ""):
    while True:
        try:
            return int(input(Texto))
        except ValueError:
            print("Insira um número")

Jogadas = []
Resultado = Apostas()
Acertos = 0
for i in range(6):
    while True:
        num = UserInput(f"Insira o seu {i+1}° número: ")
        if num not in Jogadas:
            if num in Resultado:
                Acertos += 1
            Jogadas.append(num)
            break

print(f"O resultado foi {Resultado}, você obteve {Acertos} acertos")