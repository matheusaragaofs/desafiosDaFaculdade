comidaKg = int(input())
eficiência = float(input())
cidade1 = str(input())
distancia1 = int(input())
cidade2 = str(input())
distancia2 = int(input())
cidade3=str(input())
distancia3 = int(input())
cidade4= str(input())
distancia4= int(input())
distanciaFinal = distancia1 + distancia2+ distancia3 + distancia4


if comidaKg == 0:
    print('Appa não vai a lugar algum sem comer!')

elif eficiência <distanciaFinal/comidaKg:
    print('Vamos de carroça mesmo!')
elif eficiência >= distanciaFinal/comidaKg and comidaKg !=0:
    print('Chegamos finalmente, agora vamos libertar Aang!')
