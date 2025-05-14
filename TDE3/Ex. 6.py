'''6. Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
1 a 20 polegadas. A conversão entre estas duas unidades é dada por:
polegada = centímetro × 2,54 (Não é não) (É sim ooops)'''
Polegada = 1
Centimetro = Polegada / 2.54

while Polegada <20:
    print(Centimetro)
    Polegada += 1
    Centimetro = Polegada * 2.54