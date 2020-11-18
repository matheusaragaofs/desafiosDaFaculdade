comidaKg = int(input())
eficiência = float(input())
distancia1 = int(input())
distancia2 = int(input())
distancia3 = int(input())
distancia4= int(input())
distanciaFinal = distancia1 + distancia2+ distancia3 + distancia4


if comidaKg == 0:
    print('Appa não vai a lugar algum sem comer!')

elif eficiência <distanciaFinal/comidaKg:
    print('Vamos de carroça mesmo!')
elif eficiência >= distanciaFinal/comidaKg and comidaKg !=0:
    print('Chegamos finalmente, agora vamos libertar Aang!')
