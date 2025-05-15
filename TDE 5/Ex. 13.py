'''Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente,
utilizando a seguinte estratégia de ordenação:
• selecione o elemento do vetor de 20 posições que apresenta o menor valor;
• troque este elemento pelo primeiro;
• repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de
menor valor com a segunda posição), depois os 18 elementos (trocando o de menor valor com a
terceira posição), depois os 17, 16 e assim por diante, até restar um único elemento, o maior
deles.'''

def UserInput(Texto = ""):
    while True:
        try:
            return int(input(Texto))
        except ValueError:
            print("Insira um número")
Input = []
Ordenada = []
for i in range (20):
    Input.append(UserInput(f"{i+1}° número"))

while len(Input) > 0:
    num = min(Input)
    Ordenada.append(num)
    Input.remove(num)

print(f'Lista ordenada: {Ordenada}')