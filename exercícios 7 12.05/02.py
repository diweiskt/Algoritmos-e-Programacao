'''
2. Demonstre com definir 2 conjuntos de números inteiros a 
seguir realizar as operações fundamentais abaixo. 
Para saber mais sobre Conjuntos, consulte a Wikipedia sobre o Assunto.

a. união entre conjuntos
b. interseção entre conjuntos
c. diferença entre conjuntos
d. obter o tamanho do conjunto
e. obter o valor máximo e mínimo do conjunto

Após cada operação, apresente o conjunto resultante.
'''

conjunto1 = set()
conjunto2 = set()

while True:
    print('Menu:')
    print('Digite "1" para inserir no Conjunto 1')
    print('Digite "2" para inserir no Conjunto 2')
    print('a. União de conjuntos')
    print('b. Interseção entre conjuntos')
    print('c. Diferença entre conjuntos')
    print('d. Obter o tamanho do conjunto')
    print('e. Obter o valor máximo e mínimo do conjunto')
    print('Digite "sair" para encerrar.')

    escolha = input('Escolha uma opção acima: ').strip()

    if escolha == 'sair':
        print('Programa encerrado.')
        break
    elif escolha == '1':
        a = int(input('Digite um número inteiro para o Conjunto 1: '))
        conjunto1.add(a)
    elif escolha == '2':
        a = int(input('Digite um número inteiro para o Conjunto 2: '))
        conjunto2.add(a)
    elif escolha == 'a':
        juncao = conjunto1 | conjunto2
        print(f'União:\n{juncao}')
    elif escolha == 'b':
        intersecao = conjunto1 & conjunto2
        print(f'Interseção:\n{intersecao}')
    elif escolha == 'c':
        diferenca = conjunto1 - conjunto2
        print(f'Diferença (Conjunto1 - Conjunto2):\n{diferenca}')
    elif escolha == 'd':
        op = input('Digite "1" para Conjunto 1 ou "2" para Conjunto 2: ')
        if op == '1':
            print(f'Tamanho do Conjunto 1: {len(conjunto1)}')
        elif op == '2':
            print(f'Tamanho do Conjunto 2: {len(conjunto2)}')
        else:
            print('Escolha inválida.')
    elif escolha == 'e':
        op = input('Digite "1" para Conjunto 1 ou "2" para Conjunto 2: ')
        if op == '1':
            if conjunto1:
                print(f'Valor Máximo: {max(conjunto1)}')
                print(f'Valor Mínimo: {min(conjunto1)}')
            else:
                print('Conjunto 1 está vazio.')
        elif op == '2':
            if conjunto2:
                print(f'Valor Máximo: {max(conjunto2)}')
                print(f'Valor Mínimo: {min(conjunto2)}')
            else:
                print('Conjunto 2 está vazio.')
        else:
            print('Escolha inválida.')
    else:
        print('Opção inválida!')



