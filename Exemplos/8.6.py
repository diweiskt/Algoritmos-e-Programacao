# funcao que verifica de modo exaustivo se numero e primo
def primo(num):
    if num <= 1 :
        return False
    # Verifica divisibilidade até o próprio número - 1
    for i in range(2, num) :  
        if num % i == 0 :
            return False
    return True

# Exemplo de uso:
numero = int(input("Digite um número para verificar se é primo: "))
if primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
