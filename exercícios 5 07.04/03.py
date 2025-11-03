'''
Escreva um algoritmo que lê dois números e em seguida exibe os números pares e os números ímpares existentes entre estes dois números.
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 <= n2:
    for numero in range(n1, n2 + 1):
        if numero % 2 == 0:
            print(f'{numero} é PAR')
        else:
            print(f'{numero} é ÍMPAR')
else: 
    for numero in range(n2, n1 + 1):
        if numero % 2 == 0:
            print(f'{numero} é PAR')
        else:
            print(f'{numero} ÍMPAR')
            
