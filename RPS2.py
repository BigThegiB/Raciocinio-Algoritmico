import random
Jogadas = {"pedra": 0,
           "papel": 1,
           "tesoura":2}
Resultados = [[0, -1, 1],
              [1, 0, -1],
              [-1, 1, 0]]
def Result(J1, J2):
       Resultado = Resultados[J1][J2]
       if Resultado == 1:
              return "Jogador 1 venceu!"
       elif Resultado == 0:
              return "Empate"
       else:
              return "Jogador 2 venceu!"

while True:
       J1 = str(input("Jogador 1: Pedra, Papel ou Tesoura?")).lower().strip()
       J2 = str(input("Jogador 2: Pedra, Papel ou Tesoura?")).lower().strip()
       if J1 in Jogadas and J2 in Jogadas:
              J1 = Jogadas[J1]
              J2 = Jogadas[J2]
              break

print(Result(J1,J2))