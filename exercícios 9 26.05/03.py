'''
Desenvolva um tradutor simples de língua estrangeira com as seguintes funcionalidades:

incluir nova palavra e sua tradução
alterar a tradução de uma palavra existente
remover a palavra do dicionário
traduzir (retornar a tradução associada com uma palavra)
listar todas as palavras do dicionário e sua traduação.
Opcionalmente, implemente em sua aplicação a leitura de um arquivo de 
entrada e a saída em um outro arquivo traduzido com os termos encontrados no dicionário.
'''

import json

dicionario = dict()
arquivo_dicionario = 'dicionario.json'

def ler(nomeArquivo):
    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write('{}')
        return {}

def salvar(nomeArquivo):
    with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, ensure_ascii=False, indent=4)

def addPalavra():
    add = input('Digite a palavra(ingl) que deseja adicionar: ').strip()
    if add in dicionario:
        print(f'ERRO: {add} já existe no dicionário.')
        return
    else:
        traducao = input(f'Agora digite a tradução(ptBr) de {add}: ').strip()
        dicionario[add] = traducao
        salvar(arquivo_dicionario) 
        print(f'[{add} - {traducao}] adicionado com sucesso!')

def updatePalavra():
    update = input('Digite a palavra(ingl) que deseja atualizar: ').strip()
    if update not in dicionario:
        print(f'ERRO: {update} não existe no dicionário.')
        return
    else:
        traducao = input(f'Agora digite a tradução(ptBr) de {update}: ').strip()
        dicionario[update] = traducao
        salvar(arquivo_dicionario)
        print(f'[{update} - {traducao}] atualizado com sucesso!')

def removePalavra():
    remove = input('Digite a palavra(ingl) que deseja remover: ').strip()
    if remove not in dicionario:
        print(f'ERRO: [{remove}] não existe no dicionário.')
    else:
        del dicionario[remove]
        salvar(arquivo_dicionario)
        print(f'[{remove}] removida com sucesso!')

def traduzir():
    palavra = input('Digite a palavra(ingl) que deseja traduzir: ').strip()
    if palavra not in dicionario:
        print(f'ERRO: [{palavra}] não existe no dicionário.')
    else:
        print(f'Tradução: [{dicionario[palavra]}]')

def listarDicionario():
    if not dicionario:
        print('Dicionário vazio.')
    else:
        print('\nPalavras e traduções no dicionário:')
        for palavra, traducao in dicionario.items():
            print(f'{palavra} -> {traducao}')

def main():
    global dicionario
    dicionario = ler(arquivo_dicionario)

    while True:
        print('\nMenu de opções')
        print('1. Adicionar palavra a dicionário')
        print('2. Atualizar tradução de palavra')
        print('3. Remover palavra do dicionário')
        print('4. Traduzir palavra')
        print('5. Listar todas as palavras e traduções do dicionário')
        print('0. Encerrar programa')

        opcao = input('Escolha uma opção (0-5): ').strip()

        if opcao == '0':
            print('\nPrograma encerrado!')
            break
        elif opcao == '1':
            addPalavra()
        elif opcao == '2':
            updatePalavra()
        elif opcao == '3':
            removePalavra()
        elif opcao == '4':
            traduzir()
        elif opcao == '5':
            listarDicionario()
        else:
            print('ERRO: Opção inválida.')

if __name__ == '__main__':
    main()