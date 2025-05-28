def CalcularSegundos(dias):
    return dias * 86400
def InputDias(Texto = ""):
    while True:
        try:
            num = int(input(Texto))
            if num >= 0:
                return num
            print("Insira uma quantidade não negativa")
        except ValueError:
            print("Insira um número válido de dias")

Dias = InputDias("Insira o número de dias")
Plural = "dias" if Dias != 1 else "dia"
print(f"{Dias} {Plural} tem {CalcularSegundos(Dias)} segundos")

