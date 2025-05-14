Preco = float(input('Qual o preço do produto?'))
print('As opções de pagamento são:')
print('Opção 1: A vista: 8% de desconto')
print('Opção 2: 2 parcelas com 4% de desconto')
print('Opção 3: 3 parcelas sem desconto')
print('Opção 4: 4 parcelas com 4% de acréscimo')

Pagamento = int(input('Qual opção deseja usar para o pagamento? '))

if Pagamento == 1:
    print('O produto vai custar R$', round(float(Preco-(Preco*8/100)),2))
elif Pagamento == 2:
    print('O produto vai custar duas parcelas de R$', round(float((Preco-(Preco*4/100))/2),2))
elif Pagamento == 3:
    print('O produto vai custar três parcelas de R$', round(float(Preco/3),2))
elif Pagamento == 4:
    print('O produto vai custar 4 parcelas de R$', round(float((Preco + (Preco*4/100))/4),2))
else:
    print('Opção Inválida')


