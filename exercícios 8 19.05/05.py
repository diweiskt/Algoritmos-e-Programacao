'''
Escreva uma função Python que recebe um vetor de inteiros de qualquer tamanho e informe 
se os elementos do array estão classificados em ordem crescente, ou seja, 
ordenados do menor para o maior. A função deverá retornar um valor true ou false.
'''

def estaOrdenados(vetor):
    ordenado = True
    anterior = vetor[0]
    for x in vetor[1:]:
        if int(x) < int(anterior):
            ordenado = False
            break
        anterior = x
    return ordenado

lista_numeros = []

while True:
    n = input('Digite um número ("sair" para encerrar): ')
    if n.lower() == 'sair':
        break
    lista_numeros.append(n)

if len(lista_numeros) > 0:
    print('Está ordenado?' , estaOrdenados(lista_numeros))
else:
    print('Nenhum número foi digitado.')