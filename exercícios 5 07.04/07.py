'''
Elaborar um algoritmo que leia 10 números diferentes de zero. 
Para cada número lido, o algoritmo deverá exibir uma mensagem informando se o número é positivo ou negativo. 
Caso o zero seja informado, este não deve ser contado como uma leitura válida e uma mensagem deve ser exibida ao usuário.
'''

numeros = []
for i in range(10):
    while True:  # Loop para garantir entrada válida (diferente de zero)
        try:
            numero = int(input(f'Digite o {i+1}º número: '))
            if numero == 0:
                print('Número inválido. Digite um número diferente de zero.')
            else:
                break  # Sai do loop se o número for diferente de zero
        except ValueError:
            print('Entrada inválida. Digite um número válido.')

    if numero > 0:
        print('Positivo')
    else:
        print('Negativo')

    

    