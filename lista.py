
lista_compras = []

while True:
    print("O que deseja fazer?")
    print("1. Adicionar um item à lista de compras")
    print("2. Remover um item da lista de compras")
    print("3. Listar os itens da lista de compras")
    print("4. Sair do programa")
    

    escolha = input("Digite o número da opção desejada: ")
    

    if escolha == "1":
        item = input("Digite o nome do item que deseja adicionar: ")
        lista_compras.append(item)
        print(f"O item '{item}' foi adicionado à lista.")
    

    elif escolha == "2":
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            item = input("Digite o nome do item que deseja remover: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"O item '{item}' foi removido da lista.")
            else:
                print(f"O item '{item}' não está na lista.")

    elif escolha == "3":
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            print("Lista de compras:")
            for item in lista_compras:
                print(f"- {item}")
    

    elif escolha == "4":
        print("Obrigado por utilizar o programa!")
        break

    else:
        print("Escolha inválida. Por favor, tente novamente.")