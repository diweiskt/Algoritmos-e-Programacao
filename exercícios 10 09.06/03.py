'''
Elabore um programa que implementa o Jogo da Velha utilizando uma matriz de 
elementos 3 x 3 para armazenar as jogadas. Abaixo, é sugerida uma interface 
no console para interação com o programa.
'''

def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print("\n   1 | 2 | 3")
    print("  ---+---+---")
    print("   4 | 5 | 6")
    print("  ---+---+---")
    print("   7 | 8 | 9\n")

    for i, linha in enumerate(tabuleiro):
        print(" " + " | ".join(linha))
        if i < 2:
            print("---+---+---")

def verificar_vitoria(tabuleiro, jogador):
    # Linhas, colunas e diagonais
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[linha][coluna] != ' ' for linha in range(3) for coluna in range(3))

def converter_posicao(pos):
    posicoes = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return posicoes.get(pos)

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'

    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            escolha = int(input("Escolha uma posição (1-9): "))
        except ValueError:
            print("Por favor, digite um número válido entre 1 e 9.\n")
            continue

        pos = converter_posicao(escolha)
        if not pos:
            print("Posição inválida. Digite um número de 1 a 9.\n")
            continue

        linha, coluna = pos
        if tabuleiro[linha][coluna] != ' ':
            print("Essa posição já está ocupada. Tente outra.\n")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"\nParabéns! Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("\nEmpate! Ninguém venceu.")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogar()