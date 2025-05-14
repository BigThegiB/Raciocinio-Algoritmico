'''
Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os
valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao
intervalo, ou seja, intervalo aberto.
'''

LimiteInicial = int(input('Limite Inicial: '))
LimiteFinal = int(input('Limite Final: '))
ContadorLimite = LimiteInicial + 1
while ContadorLimite <= LimiteFinal - 1:
    if ContadorLimite % 3 == 0:
        print(ContadorLimite)
    ContadorLimite += 1