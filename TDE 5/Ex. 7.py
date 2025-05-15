'''Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular.'''

Entrada = int(input('Entre um numero: '))
Triangular = False
for i in range(Entrada):
    Triangulo = (i)*(i+1)*(i+2)
    if Triangulo == Entrada:
        print(f'{Entrada} é triangular')
        Triangular = True
        break

if not Triangular:
    print(f'{Entrada} não é triangular')

