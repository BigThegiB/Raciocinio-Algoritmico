Numero1 = float(input('Número 1: '))
Numero2 = float(input('Número 2: '))
Numero3 = float(input('Número 3: '))
if Numero1 == Numero2 == Numero3:
    print('Todos os números tem o mesmo valor')
elif Numero2 <= Numero1 >= Numero3:
    print('O maior número é', Numero1)
elif Numero1 <= Numero2 >= Numero3:
    print('O maior número é:', Numero2)
elif Numero2 <= Numero3 >= Numero1:
    print('O maior número é:', Numero3)