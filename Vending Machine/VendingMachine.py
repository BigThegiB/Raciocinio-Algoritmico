import Extra
Bebidas = [ #Id, Nome, Preço, Estoque
    [1, "Coca-cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

Notas = [  # Valor, Quantidade
    [200, 5],
    [100, 5],
    [50, 5],
    [20, 5],
    [10, 5],
    [5, 5],
    [2, 5],
    [1, 5],
    [0.10, 5],
    [0.1, 5]
]
def UserInput(Texto = ""):
    while True:
        try:
            return float(input(Texto))
        except ValueError:
            print("Insira um valor válido")

def PegarPosição(BebidaID): # Pega a Posição da bebida baseada no ID (Poderia só fazer -1 mas assim fica mais bonitinho)
    BebidaID = int(BebidaID)
    for pos in range(len(Bebidas)):  #Roda pela Matriz
        if BebidaID == Bebidas[pos][0]: #Checa se o ID é igual ao item 0 da linha
            return pos #Retorna a posição do id na matriz
    return 0 # Retorna 0 em caso de não funcionar
            

def ChecarEstoque (BebidaPos): # Check para o estoque disponivel da bebida
    if Bebidas[BebidaPos][3] > 0: # Olha a quarta posição da linha do item
        return True # retorna true caso haja estoque
    else: return False # Se não houver, retorna false

def Pagamento(Pagamento,BebidaPos):
    if Pagamento >= Bebidas[BebidaPos][2]:
        Troco = Pagamento - Bebidas[BebidaPos][2]
        TrocoLista = CalcularTroco(Notas,Troco)
        if TrocoLista != Notas:
            print(f"Pagamento aprovado!")
            Bebidas[BebidaPos][3] -= 1
            return TrocoLista #Botar Função para imprimir matriz aq(oudps)
        else:
            print("Não foi possível processar o seu troco, favor inserir uma quantia diferente")
            return -1
    else: 
        print("Seu pagamento é inválido!")
        return -1
    
def CalcularTroco(Notas,Troco):
    TrocoLista = [  # Valor, Quantidade
    [200, 0],
    [100, 0],
    [50, 0],
    [20, 0],
    [10, 0],
    [5, 0],
    [2, 0],
    [1, 0],
    [0.10, 0],
    [0.1, 0]
    ]
    NotasDupe = Extra.DuplicarMatriz(Notas)

    for i in range(len(Notas)):
        while float(Notas[i][0]) <= Troco and Notas[i][1] != 0: #Checa o valor da nota e se tem estoque
            Notas[i][1] -= 1
            Troco -= float(Notas[i][0])
            TrocoLista[i][1] += 1
    if Troco == 0:
        return Extra.Remover0s(TrocoLista,1)
    else:
        return NotasDupe
    
BebidaPos = 0
while True:
    while BebidaPos == 0:
        SelUser = UserInput("Insira o ID do produto")
        BebidaPos = PegarPosição(SelUser)
        if BebidaPos != 0:
            break
        print("ID Inválido")
    while True:
        if (ChecarEstoque(BebidaPos)):
            PagamentoUser = UserInput(f"O produto custa R${Bebidas[BebidaPos][2]}\nInsira o valor pago")
            TrocoUser = CalcularTroco(Notas,PagamentoUser)
            print(TrocoUser)
            if TrocoUser != -1:
                Extra.PrintMatriz(TrocoUser,"O seu troco é:")
                break

        





# Checkar se Lista recebida é diferente da original de troco
# Caso seja continuar
# Caso não seja, pedir outro pagamento do usuário
'''def Extra(Pin):
    if Pin != 0000:
        return
    else:
        escolha = UserInput(f"1 - Editar/n2 - Adicionar\n 3 - Remover")'''