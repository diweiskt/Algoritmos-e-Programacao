'''
Elabore uma aplicação em Python que implemente um jogo de Adivinhar o 
Número de 0 a 100 com as seguintes características:

para geração do número oculto, utilizar a biblioteca Random
o jogador terá um número de chances para acertar o número. 
Se não conseguir, a aplicação deverá mostrar qual era o número oculto
a cada jogada, a aplicação deverá informar o número de tentativas restantes 
e se o número oculto é maior ou menor do o palpite do jogador
'''

import random

def advinharNumero():
    numeroOculto = random.randint(0, 100)
    chances = 5
    print('Advinhe o número!')
    while True:
        print(f'Você tem {chances} chances')
        palpite = int(input('Qual seu palpite? '))
        if (palpite == numeroOculto):
            print('Parabéns! Você acertou!')
            break
        elif (palpite < numeroOculto):
            print(f'Dica: É um número maior que {palpite}.')
        else:
            print(f'Dica: É um número menor que {palpite}.')
        chances -= 1

        if chances == 0:
            print(f'Acabaram suas chances! O número era {numeroOculto}.')

advinharNumero()