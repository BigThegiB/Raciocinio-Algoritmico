import math
# Primeira hora = 8 reais (Mínimo), depois 1.50 a cada 15 minutos
Minutos = int(input('Qual o tempo que será passado no estacionamento? (Em minutos) '))
if Minutos <= 60:
    print('Valor mínimo, R$8.00')
else:
    Valor = (1.50 * (math.floor(Minutos/15)*15))
    print('Valor fracionado, R$', Valor)

#(math.floor(Minutos/15)*15)) Serve pra arredondar o numero para a base 15 mais próxima
# Exemplo: (33/15 = 2.2), 2.2 é arredondado para 2, (2 * 15 = 30)