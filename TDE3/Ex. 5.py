# Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário.

Numero = int(input('Escolha um número: '))
Numero2 = 1
while Numero2 != Numero:
    if Numero2 % 2 != 0:
        print(Numero2)
    Numero2 += 1