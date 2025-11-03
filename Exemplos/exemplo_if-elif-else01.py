# Exemplo de if .. else
# Encontrar o maior valor entre 3 valores lidos

x = int(input("Informe valor 1: "))
y = int(input("Informe valor 2: "))
z = int(input("Informe valor 3: "))

if x > y and x > z :
    print("x é o maior")
elif y > x and y > z :
    print("y é o maior")
elif z > x and z > y :
    print("z é o maior")
else :
    print("numeros iguais")