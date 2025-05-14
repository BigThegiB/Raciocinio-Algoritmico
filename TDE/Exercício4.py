#Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores:
#(1) a vista com 5% de desconto;
#(2) o valor da parcela em 2x;
#(3) o valor da parcela em 3x com acréscimo de 5%.

Produto = float(input('Qual o valor do produto?'))

# (1)
option1 = Produto - (Produto*5/100)
# (2)
option2 = Produto / 2
# (3)
option3 = (Produto + (Produto*5/100)) / 3

print('Suas opções são:')
print('(1)','R$', option1, 'à vista')
print('(2)', "2x de",'R$', option2)
print('(3)', '3x de','R$', option3)