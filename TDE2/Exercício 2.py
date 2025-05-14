#Idade em 2023 e se idade >= 18
anoNascimento = int(input('Que ano você nasceu?'))
Idade = 2023 - anoNascimento
if Idade >= 18:
    print('Ao final de 2023 você tinha', Idade, 'anos e poderia ter feito carteira de motorista')
else:
    print('Ao final de 2023 você tinha', Idade, 'anos e NÃO poderia ter feito carteira de motorista')
