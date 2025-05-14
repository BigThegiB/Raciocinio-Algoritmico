'''Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a
média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada.'''

Entrada = int(input('Quantas idades serão calculadas?'))
ListaIdades = []
for Contagem in range(0, Entrada):
    Idade = int(input('Insira uma idade: '))
    if Idade > 0:
        ListaIdades.append(Idade)

Media = sum(ListaIdades) / len(ListaIdades)

if 0 < Media <= 25:
    print(f'Turma Jovem - Média de {Media} anos')

elif 26 <= Media <= 60:
    print(f'Turma Adulta - Média de {Media} anos')

elif Media > 60:
    print(f'Turma Idosa - Média de {Media} anos')