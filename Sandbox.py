n = int(input('Entre um número: '))
i = 1

while i * (i + 1) * (i + 2) < n:
    i += 1

if i * (i + 1) * (i + 2) == n:
    print(f'{n} é triangular')
else:
    print(f'{n} não é triangular')
