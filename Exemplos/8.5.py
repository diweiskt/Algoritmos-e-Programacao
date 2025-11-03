'''
    Escreva uma função Python que recebe um vetor de inteiros de qualquer tamanho e informe se
    os elementos do array estão classificados em ordem crescente, ou seja, ordenados do menor
    para o maior. A função deverá retornar um valor true ou false.
'''

def estaOrdenado(vetor) :
    ordenado = True
    anterior = vetor[0]
    for x in vetor :
        if int(x) < int(anterior) :
            ordenado = False
        anterior = x
    return ordenado


valores = [5, 7, 9, 11, 15]
print(estaOrdenado(valores))