saldo = float(input())
qtd_de_produtos = int(input())
produtos=  {}
for _ in range(qtd_de_produtos):
    produto = input().split()
    produtos[produto[0]] = int(produto[1])
gasto = 0
qtd_de_compras = int(input())
for _ in range(qtd_de_compras):
    produtoY = input()
    gasto += produtos[produtoY]
print(f'Terminei o mes com {saldo-gasto} reais')
