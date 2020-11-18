row_column = int(input())
matrix_values = []
for x in range(row_column):
    matrix_values.append(list(map(int,input().split())))
    


# # Calcular as linhas 
def calcular_linhas (matrix):
    # Primeira linha como base 
    soma_linhas_base=  sum(matrix_values[0])
    tamanhoLinhas = len(matrix_values)
    cont_linhas = 0

    for x in range(len(matrix_values)):
        if sum(matrix_values[x]) == soma_linhas_base:
            cont_linhas+=1

    if cont_linhas == tamanhoLinhas:
        return soma_linhas_base
    else:
        return 1
 


# Calcular as colunas
#Pegando valores dos elementos das colunas
def calcular_colunas(matrix):
    tamanho_colunas = [ ]
    for x in range(len(matrix_values)):
        for y in range(len(matrix_values)):
            tamanho_colunas.append(matrix_values[y][x])
            
    #Agrupando os elementos em colunas
    colunas_agrupadas =[ ]
    for j in range(0,len(tamanho_colunas)+1,row_column):
        ponto= j+row_column
        colunas_agrupadas.append(tamanho_colunas[j:ponto])

    #Verificando se a soma das colunas é igual
    soma_coluna_base = sum(colunas_agrupadas[0])
    cont_colunas = 0
    for w in colunas_agrupadas:
        if sum(w) == soma_coluna_base:
            cont_colunas+=1
    if cont_colunas == row_column:
        return soma_coluna_base
    else:
        return 2
    


# Calcular Diagonais
def calcular_diagonais(matrix):
    diagonais = [  ]
    for x in range(len(matrix_values)):
        diagonais.append(matrix_values[x][x])

    soma_diagonais = sum(diagonais)
    if soma_diagonais == calcular_linhas(matrix_values) and soma_diagonais == calcular_colunas(matrix_values):
        return soma_diagonais
    else:
        return 3
    


if calcular_linhas(matrix_values) == calcular_colunas(matrix_values) == calcular_diagonais(matrix_values):
    print("A matriz e magica")

else:
    print("A matriz nao e magica")

# print(calcular_linhas(matrix_values),calcular_colunas(matrix_values),calcular_diagonais(matrix_values))
