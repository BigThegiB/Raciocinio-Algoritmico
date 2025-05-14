# Fotocópia -> 0,25 se cópias < 100 e 0,20 se cópias >= 100

Copias = int(input('Quantas cópias vão ser tiradas? '))
#Achei interessante botar uma clausula caso o usuario insira um numero negativo por acidente
if Copias < 0:
    Copias = Copias * -1

if Copias < 100:
    Valor = Copias * 0.25
elif Copias >= 100:
    Valor = Copias * .20
#Poderia ter usado Else mas elif fica mais bonitinho
print(Copias,'cópias vão custar R$', Valor)
