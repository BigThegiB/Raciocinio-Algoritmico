Altura = float(input('Qual a sua altura em metros? '))
Sexo = int(input('Qual o seu sexo? (Utilize 1 para masculino e 2 para feminino) '))

if Sexo == 1:
    Peso = (72.7 * Altura) - 58
    print('Seu peso ideal é', round(Peso, 2), 'KG')
elif Sexo == 2:
    Peso = (62.1 * Altura) - 44.7
    print('Seu peso ideal é', round(Peso, 2), 'KG')
else:
    print('Sexo invalido')
