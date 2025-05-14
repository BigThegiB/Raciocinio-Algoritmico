#1 quilograma = 2,20462262 libras

PesoQuilos = float(input('Qual o seu peso em kilos? '))
PesoLibras = PesoQuilos * 2.20462262

if PesoLibras < 161:
    print('Categoria inferior a Super-Médio')
elif 161 <= PesoLibras < 169:
    print('Categoria Super-Médio')
elif PesoLibras <= 175:
    print('Categoria Meio-Pesado')
elif PesoLibras <= 200:
    print('Categoria Cruzador')
elif PesoLibras >= 201:
    print('Categoria Peso-Pesado')