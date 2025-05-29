Distancias = [
    [0,    310,  716,   408,   852],
    [310,  0,    470,   705,  1144],
    [716,  470,  0,    1119,  1553],
    [408,  705,  1119,  0,     429],
    [852,  1144, 1553,  429,   0]
]

Cidades = {
    "curitiba": 0,
    "florianopolis": 1,
    "porto alegre": 2,
    "sao paulo": 3,
    "rio de janeiro": 4
}

def CityInput(Texto = ""):
        while True:
            CidadeInput = str(input(Texto)).lower().strip().replace("á", "a").replace("ã", "a")
            print (CidadeInput)
            if CidadeInput in Cidades:
                return CidadeInput
            print("Insira uma cidade válida")

def CalcularDistancia(Cidade1,Cidade2):
            Cidade1 = Cidades[Cidade1]
            Cidade2 = Cidades[Cidade2]
            Distancia = Distancias[Cidade1][Cidade2]
            return Distancia

Cidade1 = CityInput("Insira a cidade de origem")
Cidade2 = CityInput("Insira a cidade de destino")

print(f"A distância entre {Cidade1.title()} e {Cidade2.title()} é de {CalcularDistancia(Cidade1,Cidade2)} KM")

