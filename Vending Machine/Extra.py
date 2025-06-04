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


def Remover0s(Matriz,Coluna):
    MatrizDupe = []
    for i in range(len(Matriz)):
        if Matriz[i][Coluna] != 0:
            MatrizDupe.append(Matriz[i])
    return MatrizDupe

def DuplicarMatriz(Matriz):
    MatrizDupe = [coluna[:] for coluna in Matriz] # [:] serve para dividir uma parte especifica da matriz, mas também retorna os valores de verdade, diferente do append q só referencia
    return MatrizDupe #Cont. Então o código está pegando cada linha da matriz e fazendo uma cópia da seção que foi dividida, como o [:] não está recebendo valores, copia a linha toda


def PrintMatriz (Matriz, Mensagem = ""):
    print(Mensagem)
    for linha in Matriz:
        print(linha)


