import random

Opcoes = ("Pedra", "Papel", "Tesoura")
AI1 = random.choice(Opcoes)
AI2 = random.choice(Opcoes)
Continuar = "y"
while Continuar == 'y':
    if AI1 == "Pedra":
        if AI2 == "Pedra":
            print('Empate')
        elif AI2 == "Papel":
            print('Jogador 2 Venceu')
        elif AI2 == "Tesoura":
            print("Jogador 1 Venceu")
    elif AI1 == "Tesoura":
        if AI2 == "Pedra":
            print('Jogador 2 Venceu')
        elif AI2 == "Papel":
            print('Jogador 1 Venceu')
        elif AI2 == "Tesoura":
            print("Empate")

    elif AI1 == "Papel":
        if AI2 == "Pedra":
            print('Jogador 1 Venceu')
        elif AI2 == "Papel":
            print('Empate')
        elif AI2 == "Tesoura":
            print("Jogador 2 Venceu")
    AI1 = random.choice(Opcoes)
    AI2 = random.choice(Opcoes)
    Continuar = input('Continuar? Y/N')