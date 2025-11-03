'''
Leia as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''

alunos = []
media7 = []
for x in range(10):
    nome = input(f'Digite o nome do {x+1}⁰ aluno: ')
    nota1 = float(input('Digite a 1⁰ nota: '))
    nota2 = float(input('Digite a 2⁰ nota: '))
    nota3 = float(input('Digite a 3⁰ nota: '))
    nota4 = float(input('Digite a 4⁰ nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    aluno = {'nome': nome, 'media': media}
    alunos.append(aluno)
    if media >= 7:
        media7.append(aluno)
print('Número de alunos na média (7.0 ou mais):', len(media7))
print('Médias dos alunos:')
for aluno in alunos:
    print(f'{aluno["nome"]}: {aluno["media"]:.2f}')
    
