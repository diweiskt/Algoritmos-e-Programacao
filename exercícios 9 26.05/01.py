'''
Leia um texto interativamente através da linha de comando e retorna 
a contagem da ocorrência de cada letra do alfabeto no texto.
'''

def contar_letras(frase):
    contagem = {}
    for letra in frase:
        if letra.isalpha():
            letra = letra.upper()
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1
    return contagem

frase_entrada = input("Digite uma frase para contar as letras: ")
resultado_contagem = contar_letras(frase_entrada)
print("Contagem de letras:")
for letra, quantidade in resultado_contagem.items():
    print(f"{letra}: {quantidade}")
print("Como esta armazenado: ", resultado_contagem)