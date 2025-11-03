'''
(Desafio) Escreva um algoritmo que retorne os números primos existentes entre 1 e 1000.
'''
print('Números primos entre 1 e 1000:')
primos = []
for numero in range(2, 1001):
    é_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            é_primo = False
            break
    if é_primo:
        primos.append(numero)

print(primos)
