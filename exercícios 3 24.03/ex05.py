'''
5. Elabore um algoritmo que leia o nome e a idade de três pessoas e após a leitura escreva 
o nome da pessoa mais velha e o nome da pessoa mais nova. Considere que não existem idades iguais.
'''

nome1 = input('Digite o primeiro nome: ')
idade1 = int(input('Digite a idade do primeiro nome: '))
while True:
    nome2 = input('Digite o segundo nome: ')
    idade2 = int(input('Digite a idade do segundo nome: '))
    if idade2 == idade1:
        print('Erro: A idade deve ser diferente da primeira pessoa. Tente novamente.')
    else:
        break
while True:
    nome3 = input('Digite o terceiro nome: ')
    idade3 = int(input('Digite a idade do terceiro nome: '))
    if idade3 == idade1 or idade3 == idade2:
        print('Erro: A idade deve ser diferente das outras pessoas. Tente novamente.')
    else:
        break
if idade1 > idade2 and idade1 > idade3:
    mais_velha = nome1
elif idade2 > idade1 and idade2 > idade3:
    mais_velha = nome2
else:
    mais_velha = nome3
if idade1 < idade2 and idade1 < idade3:
    mais_nova = nome1
elif idade2 < idade1 and idade2 < idade3:
    mais_nova = nome2
else:
    mais_nova = nome3
print(f'Pessoa mais nova: {mais_nova}')
print(f'Pessoa mais velha: {mais_velha}')