valor = int(input())
moedas100 = valor//100
valor = valor%100
moedas50 = valor//50
valor = valor%50
moedas25 = valor//25
valor = valor%25
moedas10 = valor//10
valor = valor%10
moedas5 = valor//5
valor = valor%5
moedas1 = valor//1
valor = valor%1
totmoedas = moedas100 + moedas50 + moedas25 + moedas10 + moedas5+ moedas1
if  totmoedas>0:
    print(f'{totmoedas} foi o total de moedas obtidas apos a troca')
if moedas100>0:
    print(f'{moedas100} moedas de 100')
if moedas50 > 0:
    print(f'{moedas50} moedas de 50')
if moedas25 > 0:
    print(f'{moedas25} moedas de 25')
if moedas10 > 0:
    print(f'{moedas10} moedas de 10')
if moedas5 > 0:
    print(f'{moedas5} moedas de 5')
if moedas1 > 0:
    print(f'{moedas1} moedas de 1')