
print('Favor inserir todas as notas a serem calculadas')
nota1 = float(input('Nota 1: '))

nota2 = float(input('Nota 2: '))

nota3 = float(input('Nota 3: '))

nota4 = float(input('Nota 4: '))

notaMedia = (nota1+nota2+nota3+nota4) / 4

print('A média do aluno é' , notaMedia , 'pontos')

if notaMedia >= 7.0:
    print('O aluno está aprovado')
else:
    print('O aluno está reprovado')
