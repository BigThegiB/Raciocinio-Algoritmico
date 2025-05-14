'''Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
No final, mostre a soma também.'''
#n/n*2-1
# import fractions < - Quero, não vou!!!!
def MMCCalculo(Numero1,Numero2):   #Obs: Peguei de um site, mas fiquei um bom tempo entendendo ele
    if Numero1 >= Numero2:
        MaiorNumero = Numero1
    else:
        MaiorNumero = Numero2
    while True:
        if(MaiorNumero % Numero1 == 0) and (MaiorNumero % Numero2 == 0):
            MMC = MaiorNumero
            break
        else:
            MaiorNumero += 1
    return MMC

Entrada = int(input('Insira um número: '))
ListaNumeros = []
Numeradores = []
Denominadores = []
for Contagem in range(1,Entrada+1):
    Numero = f"{Contagem}/{Contagem * 2 - 1}"
    Numeradores.append(Contagem)
    Denominadores.append(Contagem * 2 - 1)
for n in range(len(Denominadores)):
    




print(ListaNumeros, Numeradores, Denominadores)