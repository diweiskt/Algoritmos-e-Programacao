'''
Leia as quatro notas de 10 alunos, calcule e armazene em uma lista a
média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.

'''
mediaAlunos = list()
conta = 0

for i in range(10) :
    print("\nLendo notas do aluno ", i + 1)
    nota1 = float(input("Informe nota 1: "))
    nota2 = float(input("Informe nota 2: "))
    nota3 = float(input("Informe nota 3: "))
    nota4 = float(input("Informe nota 4: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    mediaAlunos.append(media)

for i in mediaAlunos :
    if i >= 7 :
        conta += 1

print("Alunos com media acima de 7.0: ", conta)
