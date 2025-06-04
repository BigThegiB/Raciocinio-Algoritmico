def UserInput(Type, Texto = ""):
    while True:
        try:
            return Type(input(Texto))
        except ValueError:
            print("Insira um valor válido")


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

TrocoLista = [  # Valor, Quantidade
[200, 0],
[100, 0],
[50, 2],
[20, 0],
[10, 4],
[5, 0],
[2, 0],
[1, 0],
[0.10, 0],
[0.1, 0]
]

def Remover0s(Matriz,Coluna):
    MatrizDupe = []
    for i in range(len(Matriz)):
        if Matriz[i][Coluna] != 0:
            MatrizDupe.append(Matriz[i])
    return MatrizDupe

def DuplicarMatriz(Matriz):
    MatrizDupe = []
    for i in range(len(Matriz)):
        MatrizDupe.append(Matriz[i])
    return MatrizDupe

def PrintMatriz (Matriz, Mensagem = ""):
    print(Mensagem)
    for linha in Matriz:
        print(linha)


