Altura = float(input('Qual a sua altura em metros? '))
Massa = float(input('Quantos kilos você pesa? '))
IMC = Massa / Altura**2

if IMC<18.5:
    print('Você está Abaixo do peso' )
elif IMC<=25:
    print('Você está no peso normal')
elif IMC<=30:
    print('Você está acima do peso')
else:
    print('Você está obeso')