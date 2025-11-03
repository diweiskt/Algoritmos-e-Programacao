'''
4. Desenvolva um algoritmo que leia o nome de uma pessoa, o dia e o mês de seu nascimento 
e em seguida apresente o nome da pessoa e o seu signo conforme a tabela abaixo:

Signo	    Período
Aquário	    21/1 - 18/2
Peixes	    19/2 - 20/3
Áries	    21/3 - 20/4
Touro	    21/4 - 21/5
Gêmeos	    22/5 - 21/6
Câncer	    22/6 - 22/7
Leão	    23/7 - 23/8
Virgem	    24/8 - 22/9
Libra	    23/9 - 23/10
Escorpião	24/10 - 22/11
Sagitário	23/11 - 21/12
Capricórnio	22/12 - 20/1

'''
while True:
    nome = input('Digite seu nome: ')
    dia = int(input('Digite o dia de seu nascimento: '))
    mes = int(input('Digite o mês de seu nascimento: '))
    if (mes < 1 or mes > 12) or (dia < 1 or dia > 31):
        print("Data inválida! Tente novamente.")
        continue
    if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
        signo = 'Aquário'
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo = 'Peixes'
    elif (mes == 3 and dia >=21) or (mes == 4 and dia <= 20):
        signo = 'Áries'
    elif (mes == 4 and dia >=21) or (mes == 5 and dia <= 21):
        signo = 'Touro'
    elif (mes == 5 and dia >=22) or (mes == 6 and dia <= 21):
        signo = 'Gêmeos'
    elif (mes == 6 and dia >=22) or (mes == 7 and dia <= 22):
        signo = 'Câncer'
    elif (mes == 7 and dia >=23) or (mes == 8 and dia <= 23):
        signo = 'Leão'
    elif (mes == 8 and dia >=24) or (mes == 9 and dia <= 22):
        signo = 'Virgem'
    elif (mes == 9 and dia >=23) or (mes == 10 and dia <= 23):
        signo = 'Libra'
    elif (mes == 10 and dia >=24) or (mes == 11 and dia <= 22):
        signo = 'Escorpião'
    elif (mes == 11 and dia >=23) or (mes == 12 and dia <= 21):
        signo = 'Sagitário'
    elif (mes == 12 and dia >=22) or (mes == 1 and dia <= 20):
        signo = 'Capricórnio'
    print(f'Nome: {nome}')
    print(f'Signo: {signo}')
    break
