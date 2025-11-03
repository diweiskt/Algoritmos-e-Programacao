'''
1. Leia números inteiros até que uma condição de parada seja
atingida. Após, mostre-os.
'''
#numeros = []
numeros = list()
while True :
    num = int(input("Informe um número (zero para terminar): "))
    if num == 0 :
        break
    numeros.append(num)
print(numeros)
for x in numeros :
    print(x)