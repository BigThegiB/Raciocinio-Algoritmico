Peso = float(input('Qual o peso em kg? '))

if Peso < 50:
    categoria = 'Palha'
elif Peso <= 59.99:
    categoria = "Pluma"
elif Peso <= 75.99:
    categoria = "Leve"
elif Peso <= 87.99:
    categoria = "Pesado"
elif Peso >= 88:
    categoria = 'Super Pesado'
else:
    categoria = 'Peso invalido'

print("A categoria é:", categoria)
