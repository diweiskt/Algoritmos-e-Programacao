'''
Leia duas listas com 10 elementos cada. Gere um terceira lista de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.
'''

list1 = []
list2 = []
list3 = []
for x in range(10):
    a = input(f'Digite o {x+1}⁰ elemento (lista 1): ')
    list1.append(a)
for x in range(10):
    b = input(f'Digite o {x+1}⁰ elemento (lista 2): ')
    list2.append(b)
for p, s in zip(list1, list2):
    list3.append(p)
    list3.append(s)
print(list3)
