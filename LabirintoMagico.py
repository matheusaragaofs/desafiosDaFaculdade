

linha = 0
coluna = 0

matriz = []
for i in range(10):
    linha2 = [int(x) for x in input().split()]
    matriz.append(linha2)


def percorrer_caminho(matriz, linha, coluna):
        matriz[linha][coluna]= - 1
        if linha == 9 and coluna == 9:
            return print('Esse labirinto possui saída!')
        elif linha+1 < len(matriz) and matriz[linha+1][coluna] == 1:
            percorrer_caminho(matriz, linha+1, coluna)
        elif coluna+1 < len(matriz) and matriz[linha][coluna + 1] == 1:
            percorrer_caminho(matriz, linha, coluna+1)
        elif linha != 0 and matriz[linha-1][coluna] == 1:
            percorrer_caminho(matriz, linha-1, coluna)
        elif coluna != 0 and matriz[linha][coluna-1] == 1:
            percorrer_caminho(matriz, linha, coluna-1)
        else:
            return print('Esse labirinto não possui saída!')




percorrer_caminho(matriz, linha, coluna)
