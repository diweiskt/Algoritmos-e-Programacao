'''
2. Em uma determinada cidade, a passagem escolar representa 60% do valor da passagem normal. 
Cada estudante tem direito a adquirir até 50 passagens escolares por mês letivo com desconto, 
podendo adquirir mais passagens, mas sem o desconto. Desenvolva um algoritmo que receba o valor 
da passagem normal e o número de passagens a serem adquiridas, calcule e apresente o valor da passagem 
escolar e o montante a ser pago pelas passagens adquiridas.
'''

valor = float(input('Digite o valor da passagem: '))
num = int(input('Digite o número de passagens: '))
valor_desconto = valor * 0.6
if num <= 50:
    vt = num * valor_desconto
else:
    valor_com_desconto = 50 * valor_desconto
    valor_sem_desconto = (num - 50) * valor
    vt = valor_com_desconto + valor_sem_desconto
print(f'Quantidade: {num} passagens')
print(f'Valor únitario com desconto (até 50 passagens): R${valor_desconto:.2f}')
print(f'Valor Total: R${vt:.2f}')