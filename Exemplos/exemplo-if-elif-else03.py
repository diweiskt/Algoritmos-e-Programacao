a = 44
b = 33
c = 50

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print("Maior valor: ", maior)
print("Menor valor: ", menor)
