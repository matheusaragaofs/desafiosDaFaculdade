list = [ ]
list2= [ ]
word = input()
#Vai rodar os numeros um por um
for letter in word:
    if letter == "#":
        # Se encontrar uma hashtag, ele apaga ela, apaga os dois ultimos números adicionados
        unit = list.pop()
        ten = list.pop()
        # os dois ultimos numeros apagados, vão juntar sua unidade e dezena, formando um inteiro, e por fim o adicionando
        # na lista
        full_number = (int(ten) * 10 + int(unit))
        list.append(full_number)
    else:
        #Vai adicionar numero por numero
        list.append(int(letter))

#Vai transformar os numeros da lista em letras a partir do chr, baseado no ASCII, somando os com o 96, e juntando com o
#end = '' pra não quebrar linha
for i in list:
    print(chr(i+96), end='')