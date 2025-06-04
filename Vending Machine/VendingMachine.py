import Extra
Bebidas = [ #Id, Nome, Preço, Estoque
    [1, "Coca-cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

Notas = [  # Valor, Quantidade
    [200, 0],
    [100, 0],
    [50, 0],
    [20, 1],
    [10, 0],
    [5, 0],
    [2, 0],
    [1, 0],
    [0.10, 0],
    [0.1, 0]
]
def UserInput(Texto = ""):
    while True:
        try:
            return float(input(Texto))
        except ValueError:
            print("Insira um valor válido")

def PegarPosição(BebidaID): # Pega a Posição da bebida baseada no ID (Poderia só fazer -1 mas assim fica mais bonitinho)
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
        print(f"Pagamento aprovado!\nSeu troco é de {Troco} reais")
        #Dimimuir ewstoque bebida
        return Troco
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
        while Notas[i][0] <= Troco and Notas[i][1] != 0: #Checa o valor da nota e se tem estoque
            Notas[i][1] -= 1
            Troco -= Notas[i][0]
            TrocoLista[i][1] += 1
    if Troco == 0:
        return Extra.Remover0s(TrocoLista,1)
    else:
        return NotasDupe

'''def GodMode(Pin):
    if Pin != 0000:
        return
    else:
        escolha = UserInput(f"1 - Editar/n2 - Adicionar\n 3 - Remover")'''

# Checkar se Lista recebida é diferente da original de troco
# Caso seja continuar
# Caso não seja, pedir outro pagamento do usuário