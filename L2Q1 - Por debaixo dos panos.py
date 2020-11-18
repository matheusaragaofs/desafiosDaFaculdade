tamanhoPalavra = int(input())
palavra = ' '
for x in range(tamanhoPalavra):
    letras,repetir = input().split()
    letras = chr(97+int(letras))
    for y in range(int(repetir)):
        palavra = palavra +letras
print(palavra.title())