def escapar_da_inception(começo, final, contador):
    if começo == final:
        return contador
    elif contador == 10:
        return 11
    else:
        folha1 = escapar_da_inception(começo//2, final, contador+1)
        folha2 = escapar_da_inception(começo+1, final, contador+1)
        folha3 = escapar_da_inception(começo*10, final, contador+1)
        return min([folha1, folha2, folha3])

começo = int(input()) 
final = int(input())
passos = escapar_da_inception(começo, final, 0)

if passos == 11:
    print("Alguem me tire daquiiiii!!")
elif passos == 0:
    print("Que tipo de prova e essa?")
elif passos > 0 and passos <= 5:
    print(f"Achei facil, usei apenas {passos} passos")
elif passos > 5:
    print(f"Foi com muito esforco, mas eu passei em {passos} passos!")
else:
    print("Saida nao esperada")