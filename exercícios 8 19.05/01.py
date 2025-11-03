'''
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de MÊS de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

def dataPorExtenso(ddmmyyyy):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio",
             "junho", "julho", "agosto", "setembro", "outubro",
             "novembro", "dezembro"]
    
    if len(ddmmyyyy) != 10 or ddmmyyyy[2] != '/' or ddmmyyyy[5] != '/':
        return "NULL"
    
    try:
        dia = int(ddmmyyyy[:2])
        mes = int(ddmmyyyy[3:5])
        ano = int(ddmmyyyy[6:])

        if mes < 1 or mes > 12:
            return "NULL"

        dias_por_mes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
                        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if dia < 1 or dia > dias_por_mes[mes - 1]:
            return "NULL"

        return f"{dia:02d} de {meses[mes - 1]} de {ano}"
    
    except ValueError:
        return "NULL"
    
data = input("Digite uma data(DD/MM/AAAA): ")
print(dataPorExtenso(data))
