anoNascimento = int(input('Que ano você nasceu?'))
AnoAnterior = 2024

idade = AnoAnterior - anoNascimento

MesNascimento = int(input('Em qual mês você nasceu? (de forma numérica)'))

IdadeMes = (idade*12) + MesNascimento

print('Você tem' , IdadeMes , 'meses de idade')