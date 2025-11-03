'''
Elaborar um função que receba um número inteiro com argumento e retorne se o mesmo é primo ou não.
'''

def eprimo(x):
    if x < 2:
        return 'Não é primo'
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 'Não é primo'
    
    return 'É primo'

n = int(input('Digite um número: '))
print(eprimo(n))