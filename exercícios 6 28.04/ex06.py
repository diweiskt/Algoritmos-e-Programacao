'''
Receber a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). 
'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
for x in range(12):
    temp = float(input(f'Digite a temperatura média de {meses[x]}: '))
    temperaturas.append(temp)
media_anual = sum(temperaturas) / 12
print(f'Média anual: {media_anual:.2f}°C')
print('Meses com temperatura acima da média anual:')
for x in range(12):
    if temperaturas[x] > media_anual:
        print(f'{x+1} – {meses[x]}: {temperaturas[x]:.2f}°C')