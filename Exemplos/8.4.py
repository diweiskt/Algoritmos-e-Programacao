'''
    Desenvolver uma função que receba a sigla do estado (Unidade Federativa) e retorne o
    nome do estado por extenso.
'''
import uf

sigla = input("Informe a sigla do estado: ").upper()

try :
    print(uf.estados[sigla])
except:
    print("Estado nao encontrado")
