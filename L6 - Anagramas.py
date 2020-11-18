frase1 = input().lower().replace(' ','')
frase2 = input().lower().replace(' ','')
letras1 = []
letras2 = []
dicionario = {}

for letra in frase1:
    letras1.append(letra)

for letra in frase2:
    letras2.append(letra)

letras1.sort()
letras2.sort()

dicionario[frase1]=[letras1]
dicionario[frase2]=[letras2]

if dicionario[frase1] == dicionario[frase2]:
    print('Achei um anagrama')
else:
    print("Nao e um anagrama")

