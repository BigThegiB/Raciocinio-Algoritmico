Numero1 = int(input('Número 1: '))

Numero2 = int(input('Número 2: '))

Numero3 = int(input('Número 3: '))

if Numero1 >= Numero2 and Numero1 >= Numero3:
    MaiorNumero = Numero1
    if Numero2 >= Numero3:
        SegundoMaior = Numero2
        MenorNumero = Numero3
    else:
        SegundoMaior = Numero3
        MenorNumero = Numero2

elif Numero2 > Numero1 and Numero2 >= Numero3:
    MaiorNumero = Numero2
    if Numero1 >= Numero3:
        SegundoMaior = Numero1
        MenorNumero = Numero3
    else:
        SegundoMaior = Numero3
        MenorNumero = Numero1

elif Numero3 > Numero1 and Numero3 >= Numero1:
    MaiorNumero = Numero3
    if Numero1 >= Numero2:
        SegundoMaior = Numero1
        MenorNumero = Numero2
    else:
        SegundoMaior = Numero2
        MenorNumero = Numero1

print("A ordem é:" , MaiorNumero,"," , SegundoMaior,",",MenorNumero)