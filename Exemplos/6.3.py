'''
Leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
'''
caracteres = input("Informe sequencia de caracteres: ")
listaConsoantes = list()

for i in caracteres:
    if i not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') :
        listaConsoantes.append(i)
txt = "Foram lidos {} consoantes\nSao elas:{}"
consoantes = len(listaConsoantes)
print(txt.format(consoantes, listaConsoantes))