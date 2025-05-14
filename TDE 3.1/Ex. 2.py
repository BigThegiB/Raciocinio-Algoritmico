Entrada = int(input('Entre um numero'))
Contagem = 0
for Contagem in range(Entrada):
    Triangulo = (Contagem)*(Contagem+1)*(Contagem+2)
    if Triangulo == Entrada:
        print(f'{Entrada} é triangular')
        Triangulo = True
        break

if Triangulo != True:
    print('Numero não é triangular')