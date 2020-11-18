FAang = int(input())
FSoldiers = int(input())

if FAang > FSoldiers:
    print('Aang venceu o combate!')
elif FSoldiers > FAang:
    print("Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo.")
else:

    AgAang = str(input())
    AgSoldiers = str(input())
    if AgAang =='Rapido' and AgSoldiers =='Lento':
        print('Aang venceu o combate!')
    elif AgAang == 'Lento' and AgSoldiers =='Rapido':
        print("Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo.")
    elif AgAang == 'Rapido' and AgSoldiers == 'Rapido' or AgAang == 'Lento' and AgSoldiers == 'Lento':

        PrecAang = float(input())
        PrecSoldiers= float(input())
        if PrecAang > PrecSoldiers:
            print('Aang venceu o combate!')
        elif PrecSoldiers > PrecAang:
            print("Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo.")
        elif PrecAang == PrecSoldiers:
            print('Aang venceu o combate!')


