'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que
peça um número inteiro e determine se ele é ou não um número primo.'''

Entrada = int(input('Insira um número: '))
Primo = True
for Contagem in range(2,Entrada):
    if Entrada % Contagem == 0:
        Primo = False

if Primo and Entrada > 1:
    print('Número é primo')
elif Entrada <= 1:
    print('Número inválido')
else:
    print('Número não é primo')
