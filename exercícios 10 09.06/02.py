'''
Desenvolva uma aplicação que implemente o Jogo da Forca e que, a cada execução, 
escolha uma palavra aleatória de uma lista de palavras. O jogador poderá errar 5 vezes 
antes de ser "enforcado". A lista de palavras pode ser obtida de um arquivo ou Hard-coded. 
Abaixo, é sugeridauma interface no console para interação com o programa. 
'''
import random

def escolher_palavra():
    palavras = [
        "jacare",
        "crocodilo",
        "pantano",
        "lacoste",
        "elefante",
        "girafa",
        "hipopotamo",
        "tucano"
    ]
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_certas):
    resultado = ''
    for letra in palavra:
        if letra in letras_certas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado.strip()

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_restantes = 5

    print("Bem-vindo ao Jogo da Forca!")
    print(f"Você tem {tentativas_restantes} tentativas para acertar a palavra.\n")

    while tentativas_restantes > 0:
        print(mostrar_palavra_oculta(palavra, letras_certas))
        print(f"Letras erradas: {' '.join(sorted(letras_erradas))}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra válida.\n")
            continue

        if palpite in letras_certas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.\n")
            continue

        if palpite in palavra:
            letras_certas.add(palpite)
            print("Boa! Letra correta.\n")
        else:
            letras_erradas.add(palpite)
            tentativas_restantes -= 1
            print("Letra incorreta!\n")

        # Verifica se o jogador ganhou
        if all(letra in letras_certas for letra in palavra):
            print(f"Parabéns! Você acertou a palavra: {palavra}")
            break
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar_forca()