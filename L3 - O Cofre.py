travas = int(input())
for n in range(travas):
    lista = input().split()
    tick = lista.count('tick')
    teck = lista.count('teck')
    #For pro tick:
    for x in range(tick):
        removido = lista.pop()
        lista.insert(0,removido)
    #For pro teck:
    for y in range(teck):
        primeiro = lista.pop(0)
        lista.append(primeiro)
    print(" ".join(lista).replace('tick','click').replace('teck','cleck'))