import Godmode
Bebidas = [ #Id, Nome, Preço, Estoque
    [1, "Coca-cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

Troco = { # Nota : Quantidade de notas
    0.1: 5,
    0.10: 5,
    1: 5,
    2: 5,
    5: 5,
    10: 5,
    20: 5,
    50: 5,
    100: 5,
    200: 5
}
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

def Pagamento(NotasPagas,BebidaPos):
    if sum(NotasPagas) > Bebidas[BebidaPos][2]:
        Troco = sum(NotasPagas) - Bebidas[BebidaPos][2]

'''def GodMode(Pin):
    if Pin != 0000:
        return
    else:
        escolha = UserInput(f"1 - Editar/n2 - Adicionar\n 3 - Remover")'''


Godmode.Editar(0,Bebidas)

print(Bebidas)
