orcamento = int(input())
v1 = int(input())
p1 = float(input())
v2 = int(input())
p2 = float(input())
v3 = int(input())
p3 = float(input())
mais_barato = v1
opcao = 'primeira'
cont_disponiveis = 0

if orcamento>=v1 and orcamento<v2 and orcamento<v3:
    mais_barato = v1
    opcao= 'primeira'

if v2<v1:
    mais_barato = v2
    opcao = 'segunda'

if v3<v2 and v3<v1:
     mais_barato = v3
     opcao = 'terceira'

if mais_barato == v1 and orcamento >= mais_barato and v2 > orcamento < v3:
    print(f'So me resta escolher a {opcao} opcao de imovel')

elif mais_barato == v2 and orcamento >= mais_barato and v1 > orcamento < v3:
    print(f'So me resta escolher a {opcao} opcao de imovel')

elif mais_barato == v3 and orcamento >= mais_barato and v1 > orcamento < v2:
    print(f'So me resta escolher a {opcao} opcao de imovel')

elif orcamento < v1 and orcamento < v2 and orcamento < v3:
    print(f'Nao consigo alugar nenhum imovel, eu precisaria de mais {mais_barato-orcamento} moedas')
else:
    if p1 == p2 == p3:
        print(f'Vou escolher a {opcao} opcao de imovel')
    elif p1 <= p2 and p1 <= p3:
        print(f'Vou escolher a primeira opcao de imovel')
    elif p2 <= p1 and p2 <= p3:
        print(f'Vou escolher a segunda opcao de imovel')
    elif p3 <= p1 and p3 <= p2:
        print(f'Vou escolher a terceira opcao de imovel')