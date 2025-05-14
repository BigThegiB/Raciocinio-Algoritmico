Idade = int(input('Qual a sua idade? '))

if 5 <= Idade <= 7:
    print('Categoria: Infantil A')
elif 5 < Idade<=10:
    print('Categoria: Infantil B')
elif 5 < Idade<=13:
    print('Categoria: Juvenil A')
elif 5 < Idade<=17:
    print('Categoria: Juvenil B')
elif 5 < Idade>=18:
    print('Categoria: Adulto')
else:
    print('N/A')