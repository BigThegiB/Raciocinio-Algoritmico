
Bebidas = [
    [1, "Coca-cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]


def PegarPosição(BebidaID): # Pega a Posição da bebida baseada no ID (Poderia só fazer -1 mas assim fica mais bonitinho)
    for pos in range(len(Bebidas)-1):
        if BebidaID == Bebidas[pos][0]:
            return pos
    return 0
            

def ChecarEstoque (BebidaPos):
    if Bebidas[BebidaPos][3] > 0:
        return True
    else: return False


