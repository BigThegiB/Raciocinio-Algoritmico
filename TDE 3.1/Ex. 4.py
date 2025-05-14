Base = int(input('Base: '))
ExpoenteInicial = int(input('Expoente: '))
Soma = Base
Expoente = ExpoenteInicial -1
if ExpoenteInicial != 0:
    while Expoente != 0:
        Soma = Soma * Base
        Expoente -= 1
else:
    Soma = 1
print(Soma)