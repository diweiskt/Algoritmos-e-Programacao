# define o conjunto
compras = set()
# definimos o menu
txt = '''
a. adicionar item
b. remover item
c. exibir todos os itens
d. ordernar o conjunto alfabeticamente
e. verificar se um item está contido no conjunto
f. gravar a lista de compras em um arquivo
g. ler a lista de compras de um arquivo
x. encerra aplicacao
'''
while True :
    print(txt)
    opcao = input("Informe sua opcao: ").lower()
    
    match opcao :
        case 'a' :
            item = input("Informe item a adicionar: ")
            if item in compras :
                print("Item ja está no conjunto! ")
            compras.add(item)
        case 'b' :
            item = input("Informe item a remover: ")
            compras.remove(item)
        case 'c' :
            print(compras)
        case 'd' :
            temp = list(compras)
            temp.sort()
            print("Conjunto ordenado: ", temp)
        case 'e' :
            item = input("Informe item a procurar: ")
            if item in compras :
                print("Item ja está no conjunto! ")
        case 'f' :
            f = open("lista.txt","w")
            for i in compras :
                f.writelines(i + "\n")
            f.close()
        case 'g' :
            f = open("lista.txt","r")
            compras.clear()
            for i in f.readlines() :
                compras.add(i.replace("\n", ""))
            f.close()
        case 'x' :
            break
            # tambem pode utilizar exit()

