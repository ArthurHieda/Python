#Arthur Hieda Cunha Rm551882

dicionario = {}

def preencher(dicionario):
    if len(dicionario) >= 4:
        print("O dicionário já contém 4 registros.")
        return
    while len(dicionario) < 4:
        cam = input("Campo:")
        val = input("Valor:")
        dicionario[cam] = val
    print(dicionario)

def editar_valores(dicionario):
    while True:
        print(dicionario)
        print("1 - Deletar")
        print("2 - Substituir")
        print("3 - Voltar para o menu")
        esc2 = int(input("Digite o número da opção desejada:"))
        if esc2 == 1:
            cam2 = input("Qual campo você gostaria de excluir?")
            if cam2 in dicionario:
                del dicionario[cam2]
            else:
                print("Campo não encontrado.")
        elif esc2 == 2:
            subcam = input("Diga o campo que gostaria de substituir:")
            if subcam in dicionario:
                novo_valor = input("Digite o novo valor:")
                dicionario[subcam] = novo_valor
            else:
                print("Campo não encontrado.")
        elif esc2 == 3:
            return

def mostrar(dicionario):
    print(dicionario)

def menu():
    while True:
        print("MENU:")
        print("1 - Preencher registros")
        print("2 - Exibir registros")
        print("3 - Editar")
        print("4 - Sair")
        escolha = int(input("Escolha uma opção:"))
        if escolha == 1:
            preencher(dicionario)
        elif escolha == 2:
            mostrar(dicionario)
        elif escolha == 3:
            if not dicionario:
                print("O dicionário está vazio.")
                continue
            editar = input("Deseja alterar algum valor? [S]im ou [N]ão:")
            if editar == "N":
                menu()
            elif editar == "S":
                editar_valores(dicionario)
        elif escolha == 4:
            print("Saindo do programa.")
            break

menu()

