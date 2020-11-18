lista = []
nome = str(input())
b1 = str(input())
b2 = str(input())
b3 = str(input())
b4 = str(input())

lista.append(b1)
lista.append(b2)
lista.append(b3)
lista.append(b4)


count = 0

for item in lista:
    if item in lista and item == 'macaco de madeira' or item == 'pirocoptero' or item =='tambor de mao de madeira' or item =='tartaruga de barro' :
        count +=1
if count == 4:
    print(f'{nome} eh o avatar.')
else:
    print(f'{nome} nao eh o avatar.')
