'''
Elabore uma função que receba três valores representando os lados de um triângulo e retorno o tipo do triângulo. 
(já resolvemos esse sem funções)
'''

def triangulo(a, b, c):
    if (a + b) <= c or (b + c) <= a or (a + c) <= b :
        return "Nao forma triangulo"
    elif a == b and b == c :
        tipo = "Equilatero"
    elif a != b and b != c and a != c :
        tipo = "Escaleno"
    else :
        tipo = "Isosceles"
    
    return tipo

a = int(input('Informe o valor do lado a do triângulo: '))
b = int(input('Informe o valor do lado b do triângulo: '))
c = int(input('Informe o valor do lado c do triângulo: '))
print('Tipo do triângulo:', triangulo(a, b, c))