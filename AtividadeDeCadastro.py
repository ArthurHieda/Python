import os

def preenche_registros(t: list, reg: dict) -> None:
    while True:
        x = input("Instagram:")
        if x != '.':
            novo_registro = {}
            novo_registro['instagram'] = x
            novo_registro['nome'] = input("Nome: ")
            novo_registro['celular'] = input("Celular: ")
            t.append(novo_registro)
        else:
            break

def pesquisa(insta: str, t: list) -> bool:
    for i, registro in enumerate(t):
        if registro['instagram'] == insta:
            exibe_registro(t, i)
            return True
    return False

def preenche_registro(t: list, reg: dict) -> None:
    print("PREENCHENDO O REGISTRO")
    reg['instagram'] = input("Instagram: ")
    reg['nome'] = input("Nome: ")
    reg['celular'] = input("Celular: ")
    t.append(reg.copy())

def exibe_registro(t: list, i: int) -> None:
    print(f"\nREGISTRO.....: {i}")
    print(f"Instagram: {t[i]['instagram']}")
    print(f"Nome: {t[i]['nome']}")
    print(f"Celular: {t[i]['celular']}\n")

def exibe_tabela(t: list) -> None:
    for indice in range(len(t)):
        exibe_registro(t, indice)

def cadastro_pesquisando(t: list) -> None:
    insta = input("Instagram: ")
    encontrado = False
    for registro in t:
        if registro['instagram'] == insta:
            encontrado = True
            break
    if encontrado:
        print("Instagram já cadastrado!")
    else:
        novo_registro = {}
        novo_registro['instagram'] = insta
        novo_registro['nome'] = input("Nome: ")
        novo_registro['celular'] = input("Celular: ")
        t.append(novo_registro)
        print("Cadastro realizado com sucesso.")

def edicao_pesquisando(t: list) -> None:
    insta = input("Instagram (para pesquisa): ")
    encontrado = False
    for i, registro in enumerate(t):
        if registro['instagram'] == insta:
            encontrado = True
            print("Editando registro encontrado:")
            novo_nome = input("Novo Nome: ")
            novo_celular = input("Novo Celular (pressione Enter para manter o mesmo): ")
            if novo_celular == "":
                novo_celular = registro['celular']
            duplicado = False
            for r in t:
                if r['instagram'] == insta and r['nome'] == novo_nome:
                    duplicado = True
                    break
            if duplicado:
                print("Já existe um registro igual ao que você está tentando editar.")
            else:
                t[i]['nome'] = novo_nome
                t[i]['celular'] = novo_celular
                print("Registro atualizado com sucesso.")
            break
    if not encontrado:
        print("Instagram não cadastrado.")

tabela = list()
contato = {}

while True:
    os.system("clear")
    print("""
    0 - SAIR
    1 - CADASTRAR UM CONTATO
    2 - EXIBIR A TABELA (CONTATOS CADASTRADOS)
    3 - PREENCHE REGISTROS
    4 - PESQUISA CONTATO
    5 - CADASTRO (PESQUISANDO)
    6 - EDIÇÃO (PESQUISANDO)
    """)
    opcao = int(input("Escolha: "))

    if opcao == 0:
        break
    elif opcao == 1:
        preenche_registro(tabela, contato)
    elif opcao == 2:
        exibe_tabela(tabela)
    elif opcao == 3:
        preenche_registros(tabela, contato)
    elif opcao == 4:
        insta = input("Instagram: ")
        if not pesquisa(insta, tabela):
            print("Instagram não cadastrado!")
    elif opcao == 5:
        cadastro_pesquisando(tabela)
    elif opcao == 6:
        edicao_pesquisando(tabela)

    input("\nDigite algo para continuar...")
