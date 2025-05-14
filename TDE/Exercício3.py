#3. Faça um algoritmo que receba o salário de um profissional e calcule quantos salário mínimos ele recebe.

# Salário mínimo = R$ 1.518,00
SalarioTotal = float(input('Qual o seu salário atual?'))
SalarioMinimo = float(1518)
SalarioComparado = round(SalarioTotal / SalarioMinimo, 2)

print('Atualmente, você tem a renda de' , SalarioComparado, "salários mínimos")

# Aprendi a usar round :)