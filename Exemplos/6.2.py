''' 2. Leia uma lista de 10 números de ponto flutuante e mostre-os
na ordem inversa. '''

listaValores = []

for i in range(10) :
    listaValores.append(float(input("Informe um valor: ")))

# uma forma    
listaValores.reverse()
print(listaValores)

# outra forma
listaInversa = []
for i in range(9, -1, -1) :
    listaInversa.append(listaValores[i])
print(listaInversa)
