'''
Desenvolva um algoritmo que leia 10 números e ao final da leitura, mostre quantos, dos números lidos são positivos e quantos são negativos.
'''

negativos = 0
positivos = 0
numeros = []
for i in range(10):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
