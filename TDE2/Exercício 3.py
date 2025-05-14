import math
Inteiro = int(input("Insira um número inteiro: "))
if Inteiro >= 0:
    print('A raiz de',Inteiro,'é aproximadamente',round(math.sqrt(Inteiro), 3))
else:
    print('Valor inválido')