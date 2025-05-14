'''Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário.'''

Entrada = int(input('Insira um número '))
Primos = []
Primo = True
for Numero in range(2,Entrada+1):
    for Contagem in range(2, Numero):
        if Numero % Contagem == 0:
            Primo = False
    if Primo:
        Primos.append(Numero)
    Primo = True

print(Primos)