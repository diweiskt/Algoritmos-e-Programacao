'''
3. Elaborar um algoritmo que lê 2 valores a e b, verifica se são múltiplos 
um do outro e os escreve com a mensagem: São múltiplos ou Não são múltiplos.
'''

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a % b == 0:
    print(f'{a} é múltiplo de {b}.')
else:
    print(f'{a} não é múltiplo de {b}.')