def UserInput(Type, Texto = ""):
    while True:
        try:
            return Type(input(Texto))
        except ValueError:
            print("Insira um valor válido")

Bebidas = [ #Id, Nome, Preço, Estoque
    [1, "Coca-cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

def Editar(ItemPos,Bebidas):
    while True:
        Sel = UserInput(int,"Qual parte deseja editar?\n1- Nome\n2- Preço\n3- Estoque\n4- Cancelar")
        if 0 < Sel <= 4 : 
            break
        print("Escolha uma opção válida")
    if Sel == 1:
        Bebidas[ItemPos][Sel] = str(input("Insira o novo nome")) 
    elif Sel > 1:
        Bebidas[ItemPos][Sel] = UserInput(float,"Insira o novo valor")
    else:
        return
    print("Alteração concluída")
    return
