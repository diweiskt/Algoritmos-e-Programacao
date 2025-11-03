'''
Elabore uma função que receba três valores representando os lados
de um triângulo e retorno o tipo do triângulo. 

'''
def tipoTriangulo(a, b, c) :
    if (a + b) < c or (b + c) < a or (a + c) < b :
        raise Exception("Valores dos lados nao formam triangulo")
    elif a == b and b == c :
        tipo = "Equilatero"
    elif a != b and b != c and a != c :
        tipo = "Escaleno"
    else :
        tipo = "Isosceles"
    return tipo

print(tipoTriangulo(10, 10, 10))
print(tipoTriangulo(10, 10, 20))
print(tipoTriangulo(10, 20, 30))

# erro
print(tipoTriangulo(10, 10, 30))