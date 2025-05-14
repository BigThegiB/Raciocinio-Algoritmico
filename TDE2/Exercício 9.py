Idade = int(input('Qual a sua idade?'))

if Idade>=18 and Idade<=65:
    print('Eleitor obrigatório')
elif (Idade>=16 and Idade<18) or (Idade>65):
    print('Eleitor Facultativo')
else:
    print('Não votante')