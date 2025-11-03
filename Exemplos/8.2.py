'''
Elabore uma função que converta um horário 24 horas para a notação de
12 horas. Por exemplo, a função deve converter 14:25 em 2:25 P.M. A
entrada é dada em dois inteiros.

ex. 14:25 - 2:25 P.M
    10:15 - 10:15 A.M

'''
def converteHorario(h, m) :
    if h > 24 or h < 0 :
        raise Exception("Argumento de hora incorreto")
    if m > 60 or m < 0 :
        raise Exception("Argumento de minuto incorreto")
    
    if h > 12 :
        hr = h - 12
        sufixo = " P.M"
    else :
        hr = h
        sufixo = " A.M"
    txt = str(hr)+":"+str(m)+sufixo
    return txt

print(converteHorario(13,35))
print(converteHorario(9,25))