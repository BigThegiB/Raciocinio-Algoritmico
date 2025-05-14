'''Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.'''
Primeiro = [1,2,3,4,5,6,7,8,9,10]
Segundo = [1,2,3,4,5,6,7,8,9,10]
Count1 = 0
Count2 = 0

while Count1 != 10 and Count2 != 10:
    print(f"{Primeiro[Count1]} * {Segundo[Count2]} = {Primeiro[Count1] * Segundo[Count2]}")
    Count2 += 1
    if Count2 == 10 and Count1 != 10:
        Count1 += 1
        Count2 = 0