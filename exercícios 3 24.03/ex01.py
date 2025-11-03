'''
1. O cardápio de uma lancheria é o seguinte:

Cod	Descrição	    Preço em R$
10	Cachorro-quente	    1,10
11	Bauru simples	    1,30
12	Bauru com ovo	    1,50
13	Hamburguer	        1,10
14	Cheeseburger	    1,30
15	Refrigerante	    1,50

Elabore um programa que lê o código do item pedido, a quantidade e calcula o valor 
a ser pago pelo lanche. Considera que, a cada execução, será solicitado apenas um item.
'''

cod = int(input('Digite o código do produto: '))
qnt = int(input('Digite a quantidade: '))
mapeamento = {
    10: ("Cachorro-quente", 1.10),
    11: ("Bauru simples", 1.30),
    12: ("Bauru com ovo", 1.50),
    13: ("Hamburguer", 1.10),
    14: ("Cheeseburger", 1.30),
    15: ("Refrigerante", 1.50),
}
vl = (cod * qnt)
if cod in mapeamento:
    nome, preco = mapeamento[cod]
    print(f'{nome}: {qnt}un')
    print(f'Valor total: R${vl:.2f}')
else:
    print('Código inválido' )
    exit()