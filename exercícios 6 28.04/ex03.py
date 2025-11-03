'''
Leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima-as.
'''

caracteres_lidos = []
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
for x in range(10):
    caractere = str(input('Digite um caracter: '))
    if caractere in consoantes:
        caracteres_lidos.append(caractere)
print('Consoantes digitadas:', (caracteres_lidos))
print('Total de consoantes digitadas:', len(caracteres_lidos))
    
