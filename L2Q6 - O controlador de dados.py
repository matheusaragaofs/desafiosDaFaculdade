# from math import floor
import math
days = int(input())
qtd = 0
fat = 1
qtdDADOS= 0
fatMenor=1

for i in range(days):
    qtd = int(input())

    for c in range (qtd,1,-1):
        fat*=c

    for x in range(qtd-1,1,-1):
        fatMenor*=x
    dif = fat - fatMenor

    if dif > 900000:
         kilob = math.floor(300 * dif + dif ** (1.125))

    else:
        kilob = 30 * (dif ** 2) + 900000

    tb = kilob / (10 ** 9)
    qtdDADOS += tb
z
    if tb > (10 ** 9):
        print('Humanidade controlada')
        break
    else:
        print(f'Ate o dia {i + 1}: {qtdDADOS:.2f} TB')
    fat = fatMenor = 1

