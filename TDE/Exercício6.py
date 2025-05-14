
#Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar
#um tanque cilindro, em que são fornecidas sua altura e raio, sabendo que:
#a. A lata de tinta custa R$ 50,00
#b. Cada lata contém 5 litros
#c. Cada litro de tinta pinta 3 metros quadrados
#d. Entrada do programa: altura e raio do cilindro
#e. Saída: valor em reais e quantidade de latas

#Cilindro: AreaTotal=2πr(r+h)
#Pi = 3.14

Altura = float(input('Qual a altura do cilíndro?'))
Raio = float(input('Qual o raio do cilíndro?'))

Area = 2 * 3.14 * Raio * (Raio + Altura)

#Cada litro pinta 3 metros, logo cada lata pinta 15

#Precisava arredondar pra cima, descobri sobre Math(Ceiling)
import math
Tinta = int(math.ceil(Area / 15))

Custo = round(Tinta * 50, 2)

print('A pintura vai usar', Tinta, "latas e vai custar R$",Custo, 'Reais')