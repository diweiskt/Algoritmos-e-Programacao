'''
Desenvolva um cadastro de usuário que mantenha os dados: nome, e-mail e idade, com funcionalidades CRUD.
'''

import json

usuarios = dict()
arquivo_usuarios = 'usuarios.json'

def main():
    global usuarios
    usuarios = ler(arquivo_usuarios)

    while True:
        print('\nMenu de opções')
        print('1. Criar Usuário')
        print('2. Listar Usuários')
        print('3. Atualizar Usuário')
        print('4. Remover Usuário')
        print('0. Encerrar programa')

        opcao = input('Escolha uma opção (0-4): ').strip()

        if opcao == '0':
            print('\nPrograma encerrado!')
            break
        elif opcao == '1':
            criarUser()
        elif opcao == '2':
            listarUsers()
        elif opcao == '3':
            atualizarUser()
        elif opcao == '4':
            removerUser()
        else:
            print('ERRO: Opção inválida.')

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
        json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

def criarUser():
    email = input('Digite o email de usuário: ').strip()
    if email in usuarios:
        print('Email já existente!')
        return
    nome = input('Digite o nome de usuário: ').strip()
    while True:
        idade_str = input('Digite a idade do usuário: ').strip()
        if idade_str.isdigit() and int(idade_str) > 0:
            idade = int(idade_str)
            break
        else:
            print('Idade inválida. Digite um número inteiro positivo.')
    usuarios[email] = {'nome': nome, 'idade': idade}
    salvar(arquivo_usuarios)
    print(f'Usuário {nome} criado com sucesso!')

def listarUsers():
    if not usuarios:
        print('Nenhum usuário cadastrado.')
        return
    print('\nLista de usuários:')
    for email, info in usuarios.items():
        print(f'Email: {email} - Nome: {info["nome"]} - Idade: {info["idade"]}')

def atualizarUser():
    email = input('Digite o email do usuário que deseja atualizar: ').strip()
    if email not in usuarios:
        print('Usuário não encontrado!')
        return
    nome = input(f'Digite o novo nome para o usuário ({usuarios[email]["nome"]}): ').strip()
    while True:
        idade_str = input(f'Digite a nova idade para o usuário ({usuarios[email]["idade"]}): ').strip()
        if idade_str.isdigit() and int(idade_str) > 0:
            idade = int(idade_str)
            break
        else:
            print('Idade inválida. Digite um número inteiro positivo.')
    usuarios[email]['nome'] = nome
    usuarios[email]['idade'] = idade
    salvar(arquivo_usuarios)
    print('Usuário atualizado com sucesso!')

def removerUser():
    email = input('Digite o email do usuário que deseja remover: ').strip()
    if email not in usuarios:
        print('Usuário não encontrado!')
        return
    del usuarios[email]
    salvar(arquivo_usuarios)
    print('Usuário removido com sucesso!')

if __name__ == '__main__':
    main()
