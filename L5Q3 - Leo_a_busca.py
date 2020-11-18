
# Criando minha lista
lista = []
qtd_de_inteiros = int(input())
for x in range(qtd_de_inteiros):
    numero = int(input())
    if numero < 0:
        continue
    else:
        lista.append(numero)
lista.sort()

# Filtrando itens a serem buscados
itens_procurados = []
qtd_de_buscas = int(input())
for x in range(qtd_de_buscas):

    itens_procurados.append(int(input()))



def mizera_da_busca_binaria(lista, menor, maior, x):

    if maior >= menor:

        indice_do_meio = (maior + menor) // 2

        if lista[indice_do_meio] == x:
            return indice_do_meio

        elif lista[indice_do_meio] > x:
            return mizera_da_busca_binaria(lista, menor, indice_do_meio - 1, x)

        else:
            return mizera_da_busca_binaria(lista, indice_do_meio + 1, maior, x)

    else:
        return -1



for itens in itens_procurados:
    resultado = mizera_da_busca_binaria(lista, 0, len(lista)-1, itens)
   

    if resultado != -1:
        print(f"Pesquisa com sucesso: {(resultado)}")
    else:
        print("Pesquisa falhou: -1")
