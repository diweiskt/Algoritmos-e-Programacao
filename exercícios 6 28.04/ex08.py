'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Fulano de Tal
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Fulano de Tal
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        print('O nome do atleta é obrigatório.')
    else:
        break

saltos = []

for x in range(5):
    salto = float(input(f'Digite a distancia do {x+1}° salto: '))
    saltos.append(salto)
    media = sum(saltos) / 5
print()
print(f'Atleta: {nome}')
print(f'Primeiro Salto: {saltos[0]}')
print(f'Segundo Salto: {saltos[1]}')
print(f'Terceiro Salto: {saltos[2]}')
print(f'Quarto Salto: {saltos[3]}')
print(f'Quinto Salto: {saltos[4]}')
print()
print('Resultado Final:')
print(f'Atleta: {nome}')
print(f'Saltos: {saltos}')
print(f'Média dos saltos: {media}')



