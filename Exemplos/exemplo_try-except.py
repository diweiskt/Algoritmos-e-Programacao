try:
  # descomente a linha abaixo para ver o que acontece  
  #x = 10/0
  print(x)
except NameError:
  print("Variavel x nao foi definida")
except:
  print("Houve um erro")