# Leia a quotação do dólar do dia e uma quantidade de Reais
# a ser convertida para dólares. A final, exibir o valor
# correspondente em dólares aos Reais informados.

quotacao = float(input("Informe valor do Dólar do dia: "))
reais = float(input("Informe valor em Reais a converter: "))

conversao = reais / quotacao

print("Valor em dolares: ", conversao)
