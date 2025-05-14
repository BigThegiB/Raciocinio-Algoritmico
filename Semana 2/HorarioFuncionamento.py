Horas = int(input("Qual a hora? (Sem minutos):"))
Minutos = int(input("e os minutos? "))

if Horas == 7 and Minutos >= 30:
    print('O horário está dentro do horário de funcionamento')
elif Horas >= 8 and Horas < 23:
    print('O horário está dentro do horário de funcionamento')
elif Horas == 23 and Minutos <= 10:
    print('O horário está dentro do horário de funcionamento')
else:
    print('O horário não está dentro do horário de funcionamento')