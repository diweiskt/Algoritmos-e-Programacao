def dataPorExtenso(data) :
    meses=('janeiro','fevereiro','mar','abril','maio','junho',\
       'julho','agosto','setembro','outubro','novembro','dezembro')
    dd = data[0:2]
    mm = int(data[3:5]) - 1
    yyyy = data[6:10]

    txt = dd + " de " + meses[mm] + " de " + yyyy
    return txt