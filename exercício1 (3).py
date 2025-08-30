
contatos = []
def menu_contatos():
    while True:
        try:
            opção = int(input("1. Adicionar contato\n2. Listar contatos\n3. Buscar contato\n4. Editar contato\n5. Remover contato\n6. Sair\n"))
            if opção == 1:
                Adicionar_contato()
            elif opção == 2:
                Listar_contatos()
            elif opção == 3:
                if len(contatos) <= 0:
                    print("Não há contatos para buscar, digite outro comando\n")
                else:
                    Buscar_contato()
            elif opção == 4:
                if len(contatos) <= 0:
                    print("Não há contatos para editar, digite outro comando\n")
                else:
                    Editar_contato()
            elif opção == 5:
                if len(contatos) <= 0:
                    print("Não há contatos para remover, digite outro comando\n")
                else:
                    Remover_contato()
            elif opção == 6:
                print("Sistema encerrado com sucesso. Nos vemos mais tarde!\n")
                break
            else:
                print("Comando inválido. Insira outro comando.\n")
        except ValueError:
            print("Por favor, insira um número válido.")

def Adicionar_contato():
    contato = {}
    contato['nome'] = input("Insira o nome do contato: ")
    contato['telefone'] = input("Insira o telefone do contato: ")
    contato['email'] = input("Insira o email do contato: ")
    contatos.append(contato)
    print("Contato adicionado com sucesso. Insira um novo comando.\n")

def Listar_contatos():
    for i, contato in enumerate(contatos):
        print(f"\nNÚMERO DE REGISTRO: {i+1}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")

def Buscar_contato():
    Listar_contatos()
    try:
        opção = int(input("Insira o número de registro do contato: "))
        if 1 <= opção <= len(contatos):
            contato = contatos[opção-1]
            print(f"\nNome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}\n")
        else:
            print("Número de registro inválido.\n")
    except ValueError:
        print("Por favor, insira um número válido.\n")
def Editar_contato():
    try:
        Listar_contatos()
        opção = int(input("Insira o número de registro do contato: "))
        if 1 <= opção <= len(contatos):
            print("1.Nome do contato\n2.Telefone do contato\n3.Email do contato")
            opção2 = input("Diga que parte você quer editar\n")
            if opção2 == "1":
                opção2 = input("Digite como quer mudar o nome do comtato\n")
                contatos[opção-1]['nome'] = opção2
                print("Contato editado com sucesso")
            elif opção2 == "2":
                opção2 = input("Digite como quer mudar o telefone do comtato\n")
                contatos[opção-1]['telefone'] = opção2
                print("Contato editado com sucesso")
            elif opção2 == "3":
                opção2 = input("Digite como quer mudar o email do comtato\n")
                contatos[opção-1]['email'] = opção2
                print("Contato editado com sucesso")
            else:
                print("Comando invalido")
        else:
            print("Número de registro inválido.\n")
    except ValueError:
        print("Por favor, insira um número válido.\n")
def Remover_contato():
    try:
        Listar_contatos()
        opção = int(input("Insira o número de registro do contato: "))
        if 1 <= opção <= len(contatos):
            del contatos[opção-1]
            print("Contato removido com sucesso\n")
        else:
            print("Número de registro inválido.\n")
    except ValueError:
        print("Por favor, insira um número válido.\n")
print("Diga o que queres fazer")
menu_contatos()