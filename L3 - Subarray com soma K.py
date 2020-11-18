tamanhoLista = int(input())
lista = []
for x in range(tamanhoLista):
    lista.append(int(input()))
somaMinima = int(input())

subarrays_desejados = []
for x in range(len(lista)):
    for y in range(x, len(lista)):
        subarray = lista[x:y + 1]
        if sum(subarray) >= somaMinima:
            subarrays_desejados.append(subarray)

if len(subarrays_desejados) == 0:
    print(-1)
else:
    minimo = len(subarrays_desejados[0])
    for subarray in subarrays_desejados:
        if len(subarray) < minimo:
            minimo = len(subarray)

    print(minimo)
