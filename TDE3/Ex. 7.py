'''Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela
de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10
quilômetros.'''
Metro = 20000
Kilometro = 20
Milha = Metro / 1609.344

while Kilometro < 160:
    print(Metro,'metros são', round(Milha,2), 'Milhas')
    Kilometro += 10
    Metro = Kilometro * 1000
    Milha = Metro / 1609.344
