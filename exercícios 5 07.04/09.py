'''
Elabore um algoritmo que faça a média aritmética de qualquer quantidade de números informada pelo usuário até que uma condição de parada seja atingida. 
Mostrar a contagem de números informados e a média.
'''

soma = 0
contador = 0
print("Digite os números para calcular a média.")
print("Quando quiser parar, digite 'sair'.")
while True:
    entrada = input(f"Digite o {contador + 1}º número (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        soma += numero
        contador += 1
    except ValueError:
        print("Entrada inválida. Digite um número ou 'sair' para encerrar.")
if contador > 0:
    media = soma / contador
    print(f"\nVocê informou {contador} números.")
    print(f"A média aritmética é: {media:.2f}")
else:
    print("Nenhum número foi informado.")