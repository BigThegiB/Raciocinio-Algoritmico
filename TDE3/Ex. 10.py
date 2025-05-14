'''Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
(quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
R$1.000). Considere o câmbio do dia.'''
print('EUR -> EURO')
print('USD -> DÓLAR')
print('GBP -> LIBRA')
Codigo = input('Qual o código da moeda desejada?')
Real = 0
Euro = Real * 6.17
Dolar = Real * 5.7
Libra = Real * 7.36
if Codigo == 'EUR':
    Euro = float(input('Qual a quantidade?'))
    Real = Euro * 6.17
    if Real < 1000:
        Real += (Real * 5 / 100)
    else:
        Real += (Real * 3 / 100)
    print(Euro, 'Euros vão custar', round(Real,2), 'Reais após a comissão')

elif Codigo == 'USD':
    Dolar = float(input('Qual a quantidade?'))
    Real = Dolar * 5.7
    if Real < 1000:
        Real += (Real * 5 / 100)
    else:
        Real += (Real * 3 / 100)
    print(Dolar, 'Dólares vão custar', round(Real,2), 'Reais após a comissão')

elif Codigo == 'GBP':
    Libra = float(input('Qual a quantidade?'))
    Real = Libra * 7.36
    if Real < 1000:
        Real += (Real * 5 / 100)
    else:
        Real += (Real * 3 / 100)
    print(Libra, 'Libras vão custar', round(Real,2), 'Reais após a comissão')