'''Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário
informar várias cidades em sequência, até inserir um código finalizador. Mostre então as cidades que
compõem o roteiro fornecido, a distância de cada percurso intermediário e a distância total do roteiro
fornecido.'''

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
CidadesEscolhidas = []
CidadesCodigos = []

def CityInput():
        count = 0
        while True:
            CidadeInput = str(input(f"Insira a {count+1}ª a cidade ou 'parar'para parar o código: ")).lower().strip().replace("á", "a").replace("ã", "a")
            if CidadeInput in Cidades:
                CidadesEscolhidas.append(CidadeInput.title())
                CidadeInput = Cidades[CidadeInput]
                CidadesCodigos.append(CidadeInput)
                count += 1
            elif CidadeInput == "parar":
                 break
            else: 
                 print("Insira uma cidade válida")



def CalcularDistancias(CidadesCodigos):
    ListaDistancias = []
    for i in range(len(CidadesCodigos)):
        if i != len(CidadesCodigos)-1:
            ListaDistancias.append(Distancias[CidadesCodigos[i]][CidadesCodigos[i+1]])
    return ListaDistancias

CityInput()
ListaDistancias = CalcularDistancias(CidadesCodigos)
DistanciasString = 'km, '.join(map(str, ListaDistancias))
print(f"A sua viagem entre as cidades: {', '.join(CidadesEscolhidas)} será formada pelas seguintes distancias: {DistanciasString}km, para um total de {sum(ListaDistancias)} km")