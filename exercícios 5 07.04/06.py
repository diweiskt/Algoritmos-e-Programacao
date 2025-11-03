'''
Desenvolva um algoritmo que leia números até que a soma destes números seja maior do que 100. 
Ao final, o algoritmo deverá exibir quantos números foram lidos até que a condição de parada fosse atingida.
'''

soma = 0
contador = 0
print("Digite números até que a soma ultrapasse 100:")
while soma <= 100:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1
print(f"A soma final foi {soma}.")
print(f"Quantidade de números digitados até ultrapassar 100: {contador}")