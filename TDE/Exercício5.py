#Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l)
#solicitando como entrada a distância total percorrida (KM)
# e o volume de combustível consumido para percorre-la (litros).
Distancia = float(input("Qual a distância total percorrida? (Em KM) "))
Volume = float(input('Quantos litros foram consumidos? '))
Consumo = Distancia / Volume

print('O consumo médio do automóvel é de', Consumo, "KM/L")