import random

vitoria1 = 0
vitoria2 = 0

modo = int(input('1 - Jogador X Jogador\n2 - Jogador X Máquina\n3 - Máquina X Máquina\nSelecione o modo de jogo: '))

if modo == 1:
    while True:
        escolha1 = input('Jogador 1, faça sua escolha (pedra/papel/tesoura): ').lower().strip()
        escolha2 = input('Jogador 2, faça sua escolha (pedra/papel/tesoura): ').lower().strip()

        if escolha1 == 'pedra':
            if escolha2 == 'pedra':
                print('Empate')
            if escolha2 == 'papel':
                print('Jogador 2 Venceu!')
                vitoria2 += 1
            if escolha2 == 'tesoura':
                print('Jogador 1 Venceu')
                vitoria1 += 1

        if escolha1 == 'papel':
            if escolha2 == 'pedra':
                print('Jogador 1 Venceu!')
                vitoria1 += 1
            if escolha2 == 'papel':
                print('Empate')
            if escolha2 == 'tesoura':
                print('Jogador 2 Venceu')
                vitoria2 += 1

        if escolha1 == 'tesoura':
            if escolha2 == 'pedra':
                print('Jogador 2 Venceu')
                vitoria2 += 1
            if escolha2 == 'papel':
                print('Jogador 1 Venceu!')
                vitoria1 += 1
            if escolha2 == 'tesoura':
                print('Empate')

        opcao = input('Tentar de novo? (sim/não): ')

        if opcao != 'sim':
            print(f'Placar:\n{vitoria1} X {vitoria2}\nOs desenvolvedores:\nBruno Rogério\nGlaucia Bispo\nJaqueline Cason\nLunna Damo\nAgradecem por jogar!')
            break

elif modo == 2:
    while True:
        lista = ('pedra', 'papel', 'tesoura')
        aleatorio = random.choice(lista)
        vitoria1 = 0
        vitoria2 = 0

        escolha = input('Jogador, faça sua escolha (pedra/papel/tesoura): ').lower().strip()
        print(f'Escolha do computador: {aleatorio}')
        if escolha == 'pedra':
            if aleatorio == 'pedra':
                print('Empate')
            if aleatorio == 'papel':
                print('Computador Venceu!')
                vitoria2 += 1
            if aleatorio == 'tesoura':
                print('Jogador Venceu')
                vitoria1 += 1

        if escolha == 'papel':
            if aleatorio == 'pedra':
                print('Jogador Venceu!')
                vitoria1 += 1
            if aleatorio == 'papel':
                print('Empate')
            if aleatorio == 'tesoura':
                print('Computador Venceu')
                vitoria2 += 1

        if escolha == 'tesoura':
            if aleatorio == 'pedra':
                print('Computador Venceu')
                vitoria2 += 1
            if aleatorio == 'papel':
                print('Jogador 1 Venceu!')
                vitoria1 += 1
            if aleatorio == 'tesoura':
                print('Empate')

        opcao = input('Tentar de novo? (sim/não)')

        if opcao != 'sim':
            print(f'Placar:\n{vitoria1} X {vitoria2}\nOs desenvolvedores:\nBruno Rogério\nGlaucia Bispo\nJaqueline Cason\nLunna Damo\nAgradecem por jogar!')
            break

elif modo == 3:
    while True:
        opcoes = ('pedra', 'papel', 'tesoura')
        AI1 = random.choice(opcoes)
        AI2 = random.choice(opcoes)

        print(f'Computador um: {AI1}\nComputador dois: {AI2}')

        if AI1 == 'pedra':
            if AI2 == 'pedra':
                print('Empate')
            elif AI2 == 'papel':
                print('Computador 2 Venceu')
                vitoria2 += 1
            elif AI2 == 'tesoura':
                print('Computador 1 Venceu')
                vitoria1 += 1

        elif AI1 == 'tesoura':
            if AI2 == 'pedra':
                print('Computador 2 Venceu')
                vitoria2 += 1
            elif AI2 == 'papel':
                print('Computador 1 Venceu')
                vitoria1 += 1
            elif AI2 == 'tesoura':
                print('Empate')

        elif AI1 == 'papel':
            if AI2 == 'pedra':
                print('Computador 1 Venceu')
                vitoria1 += 1
            elif AI2 == 'papel':
                print('Empate')
            elif AI2 == 'tesoura':
                print('Computador 2 Venceu')
                vitoria2 += 1

        opcao = input('Tentar de novo? (sim/não)')

        if opcao != 'sim':
            print(f'Placar:\n{vitoria1} X {vitoria2}\nOs desenvolvedores:\nBruno Rogério\nGlaucia Bispo\nJaqueline Cason\nLunna Damo\nAgradecem por jogar!')
            break

else:
    print('Valor Inválido')

