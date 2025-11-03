'''
Elabore uma aplicação para manter uma lista de compras utilizando 
a estrutura de conjuntos com as seguintes funcionalidades:

a. adicionar item (se o item já estiver no conjunto, mostrar mensagem)
b. remover item
c. exibir todos os itens
d. ordernar o conjunto alfabeticamente
e. verificar se um item está contido em um conjunto
f. gravar a lista de compras em um arquivo (padrao lista.txt)
g. ler a lista de comprar de um arquivo (padrao lista.txt)
'''

lista = set()
while True:
    print('\nMenu de opções:')
    print('a. Adicionar item')
    print('b. Remover item')
    print('c. Exibir todos os itens')
    print('d. Ordenar o conjunto alfabeticamente')
    print('e. Verificar se um item está contido no conjunto')
    print('f. Gravar a lista de compras em um arquivo')
    print('g. Ler a lista de compras de um arquivo')
    print('Digite "sair" para encerrar.')

    opcao = input('Digite a opção desejada (a - g): ').lower()
    
    if opcao == 'sair':
        print('Programa encerrado.')
        break

    elif opcao == 'a':
        item = input('Digite o produto que deseja adicionar à lista: ')
        if item in lista:
            print('Item já encontra-se na lista!')
        lista.add(item)
    
    elif opcao == 'b':
        item = input('Digite o item que deseja remover: ')
        if item not in lista:
            print('O item não existe no conjunto!')
        else:
            lista.remove(item)
            print(f'Item {item} removido com sucesso!')

    elif opcao == 'c':
        print('Itens na lista:', lista)

    elif opcao == 'd':
        print('Itens ordenados:', sorted(lista))

    elif opcao == 'e':
        item = input('Digite o item que deseja verificar: ')
        if item in lista:
            print(f'O item "{item}" está na lista.')
        else:
            print(f'O item "{item}" não está na lista.')
    
    elif opcao == 'f':
        with open("dados.txt", "w") as arquivo:
            for x in lista:
                arquivo.write(x + "\n")
        print("Lista gravada com sucesso!")

    elif opcao == 'g':
        with open('dados.txt', 'r') as arquivo:
            for x in arquivo:
                lista.add(x.strip())
        print("Lista carregada do arquivo com sucesso!")
        print("Itens carregados:", lista)
    
    else:
        print('Opção inválida.')
