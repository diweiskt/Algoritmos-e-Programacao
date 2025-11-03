'''
Demonstre com definir 2 conjuntos de números inteiros a seguir realizar as
operações fundamentais abaixo.
Após cada operação, apresente o conjunto resultante.

'''
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# a. união entre conjuntos
uniao = conjunto1.union(conjunto2)
print("Resultado da uniao: ", uniao)

# b. interseção entre conjuntos
intersecao = conjunto1.intersection(conjunto2)
print("Resultado da intersecao: ", intersecao)

# c. diferença entre conjuntos
diferenca = conjunto1.difference(conjunto2)
print("Resultado da diferenca: ", diferenca)

# d. obter o tamanho do conjunto
print("Tamanho do conjunto 1: ", len(conjunto1))
print("Tamanho do conjunto 2: ", len(conjunto2))

# e. obter o valor máximo e mínimo do conjunto
print("Valor máximo do conjunto 1: ", max(conjunto1))
print("Valor máximo do conjunto 2: ", max(conjunto2))
print("Valor mínimo do conjunto 1: ", min(conjunto1))
print("Valor mínimo do conjunto 2: ", min(conjunto2))
