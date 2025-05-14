def MMCCalculo(Numero1,Numero2):
    if Numero1 >= Numero2:
        MaiorNumero = Numero1
    else:
        MaiorNumero = Numero2


    while True:
        if(MaiorNumero % Numero1 == 0) and (MaiorNumero % Numero2 == 0):
            MMC = MaiorNumero
            break
        else:
            MaiorNumero += 1
    return MMC


print(MMCCalculo(1,16))

