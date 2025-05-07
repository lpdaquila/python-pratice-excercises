lista_de_compras = []

while True:
    opcao = input("\nSelecione uma opção: \n [i]nserir [a]pagar [l]istar [s]air: ").lower()
    
    if opcao == 'i':
        item = input("Item: ")
        lista_de_compras.append(item)
        print("Item %s adicionado à lista.\n" % item)
        
    elif opcao == 'a':
        if len(lista_de_compras) == 0:
            print("\nLista de compras vazia.")
            continue
        item = input("Qual item você deseja apagar?: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print("Item %s removido da lista.\n" % item)
        else:
            print("Item %s não encontrado na lista.\n" % item)
            
    elif opcao == 'l':
        if len(lista_de_compras) == 0:
            print("\nLista de compras vazia.")
            continue
        print("\nLista de compras:")
        for index, item in enumerate(lista_de_compras):
            print("%d - %s" % (index, item))
    elif opcao == 's':
        print("\nSaindo do programa.")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
    
    