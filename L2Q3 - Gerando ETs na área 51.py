TodasEspecies = [ ]
especies = [ ]
BBGeradosTodasEspecies = [ ]
TodasCaracteristicas = [ ]
contadorEspecies=  0
GovernoEspecie = str(input())
contBB =0
while True:
    especie01 = str(input())
    if especie01 =='fim':
        # if contBB == 0 and BBGeradosTodasEspecies == []:
        #     break
        # else:
        for x in range(contadorEspecies):
            print( f'O bebê ET gerado é da espécie {BBGeradosTodasEspecies[x]} e tem como característica {TodasCaracteristicas[x]}')
        break


    especie02 = str(input())
    caract1 = str(input())
    caract2 = str(input())
    prob1 = int(input())
    prob2 = int(input())
    potencial1 = int(input())
    potencial2 = int(input())

    especies = [especie01, especie02, caract1, caract2, prob1, prob2, potencial1, potencial2]
    CalculoEspecie01 = (especies[4]-especies[6])**2
    CalculoEspecie02 = (especies[5]-especies[7])**2
    if CalculoEspecie01 > CalculoEspecie02:
        BBGERADO = especie01
        CaractHerdada = caract1
        if especie01 == GovernoEspecie:
            contBB+=1

    else:
        BBGERADO = especie02
        CaractHerdada = caract2
        if especie02 == GovernoEspecie:
            contBB +=1

    TodasEspecies.append(especies)
    BBGeradosTodasEspecies.append(BBGERADO)
    TodasCaracteristicas.append(CaractHerdada)
    contadorEspecies +=1
print(f'nasceram {contBB} bebês ETs da espécie {GovernoEspecie}')
