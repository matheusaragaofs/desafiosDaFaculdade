texto = input()
n = int(input())
def encontrar(texto,palavra):
        count = 0
        for i in range(len(texto)):
            if texto[i:i+len(palavra)] == palavra:
                count+=1
        if count > 0:
            return print(f"{palavra} apareceu {count} vezes no texto.")
        else:
            return print(f"{palavra} nao apareceu nenhuma vez no texto.")
for x in range(n):
    palavra = input()
    (encontrar(texto,palavra))
