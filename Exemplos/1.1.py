# Calcule a média ponderada de um aluno. Considere para isso três notas com pesos
# prova A (3)
# prova B (5)
# trabalhos (2)

provaa = float(input("Informe nota prova A: "))
provab = float(input("Informe nota prova B: "))
trabalhos = float(input("Informe nota trabalhos: "))

notaFinal = (provaa * 0.3) + (provab * 0.5) + (trabalhos * 0.2)

print(" Media final: ", notaFinal)

