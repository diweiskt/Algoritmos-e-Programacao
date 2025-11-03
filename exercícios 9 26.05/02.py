'''
Efetue a leitura de um texto a partir de um arquivo de entrada e 
apresenta a contagem da ocorrência de cada palavra do texto fazendo uso da estrutura de dados dicionário.
'''

def contar_palavras(arquivo):
    contagem_palavras = {}

    f = open(arquivo, 'r', encoding="UTF-8")

    for linha in f:
        palavras = linha.split()
        
        for palavra in palavras:

            palavra = palavra.strip('\n').lower()

            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    return contagem_palavras

def main():
    arquivo = input("Digite o caminho do arquivo de texto: ")

    try:
        contagem_palavras_resultado = contar_palavras(arquivo)

        for palavra, contagem in contagem_palavras_resultado.items():
            print(f'{palavra}: {contagem}')
    except FileNotFoundError:
        print("Arquivo não encontrado.")

main()
