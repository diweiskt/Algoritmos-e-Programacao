'''
Leia uma lista de 10 números de ponto flutuante e mostre-os na ordem inversa.
'''

list = []
for x in range(10):
    numero = float(input('Digite um número: '))
    list.append(numero)
print(list[::-1])