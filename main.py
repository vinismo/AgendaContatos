#listinha
contatos = []

#adicionar contato
def incluirContato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número telefone do contato: ")
    contato = {"Nome": nome, "Telefone": telefone}
    contatos.append(contato)
    print("Contato adicionado!")

#pesquisar contato
def pesquisarContato():
    nome = input("Digite o nome do contato: ")
    encontrado = False
    for contato in contatos:
        if contato["Nome"] == nome:
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}")
            encontrado = True
            break
    if not encontrado:
        print("Contato não encontrado.")

#atualizar contato
def atualizarContato():
    nome = input("Digite o nome do contato: ")
    for contato in contatos:
        if contato["Nome"] == nome:
            novo_telefone = input("Digite o novo número de telefone: ")
            contato["Telefone"] = novo_telefone
            print("Contato atualizado!")
            return
    print("Contato não localizado.")

#excluir contato
def excluirContato():
    nome = input("Digite o nome do contato: ")
    for contato in contatos:
        if contato["Nome"] == nome:
            contatos.remove(contato)
            print("Contato excluído!")
            return
    print("Contato não encontrado.")

#listar contatos (ordem alfabetica)
def listarContatos():
    if not contatos:
        print("\n")
        print("Sua agenda não possui contatos.")
    else:
        print("\n")
        print("Lista de Contatos:")
        contatos_ordenados = sorted(contatos, key=lambda x: x["Nome"]) #ordem alfabetica
        for contato in contatos_ordenados:
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}")

#principal
while True:
    print("\n")
    print("******************************")
    print("===== Agenda de Contatos =====")
    print("******************************")   
    print("\n")
    print("1. Incluir Contato")
    print("2. Pesquisar Contato")
    print("3. Atualizar Contato")
    print("4. Excluir Contato")
    print("5. Listar Contatos")
    print("6. Sair")
    print("\n")
  
    escolha = input("Escolha uma opção acima: ")

    if escolha == "1":
        incluirContato()
    elif escolha == "2":
        pesquisarContato()
    elif escolha == "3":
        atualizarContato()
    elif escolha == "4":
        excluirContato()
    elif escolha == "5":
        listarContatos()
    elif escolha == "6":
        print("\n")        
        print("Tchau, querido professor!")
        break
    else:
        print("\n")
        print("Opção inválida, tente novamente.")
