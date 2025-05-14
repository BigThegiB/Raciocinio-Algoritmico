'''3. Supondo que a população de um país A seja da ordem de 80.000 habitantes
 com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento'''

PopulacaoA = 80000
PopulacaoB = 200000
Ano = 0
while PopulacaoA < PopulacaoB:
    PopulacaoA += (PopulacaoA*3/100)
    PopulacaoB += (PopulacaoB*1.5/100)
    Ano += 1
print(f"Vai levar {Ano} anos para a População A ultrapassar a População B")