'''
Elabore uma função que converta um horário 24 horas para a notação de 12 horas. 
Por exemplo, a função deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
'''

def ConverterHorario(horas, minutos):
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        return 'Horário inválido'
    
    if horas < 12:
        periodo = 'AM'
    else:
        periodo = 'PM'

    hora12 = horas % 12
    if hora12 == 0:
        hora12 = 12
    
    return f'{hora12}:{minutos:02d} {periodo}'

horas = int(input('Digite uma hora(24hrs): '))
minutos = int(input('Digite um minuto(59min): '))
print(ConverterHorario(horas, minutos))