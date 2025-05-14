'''Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.'''
Numeros = []
for i in range (3):
    Numeros.append(int(input('Insira um número')))

if Numeros[0] > (Numeros[1]+Numeros[2]):
    print('O primeiro valor é maior que a soma dos outros dois')
elif Numeros[0] < (Numeros[1]+Numeros[2]):
    print('O primeiro valor é menor que a soma dos outros dois')
else:
    print('O primeiro valor é igual a soma dos outros dois')