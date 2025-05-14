Altura = float(input('Qual a sua altura em metros? '))
Massa = float(input('Quantos kilos você pesa? '))
IMC = Massa / Altura**2

if IMC >= 18.5 and IMC < 25:
    print('Seu IMC é', round(IMC, 2), 'e é considerado normal pela OMS')
else:
    print('Seu IMC é', round(IMC, 2), 'e NÃO é considerado normal pela OMS')
    print('A massa máxima para estar na faixa é de:', round(float(24.9 * Altura**2), 2))
