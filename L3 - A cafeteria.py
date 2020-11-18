jogadoresTOP=  int(input())
DistanciasY = [ ]
DistanciasX = [  ]
statusDaLista = [ ]

nomesDaLisTA=  [ ]

for i in range(jogadoresTOP):
    status, nome = input().split()
    statusDaLista.append(status)
    nomesDaLisTA.append(nome)
nomesDaLisTA.extend((nomesDaLisTA))
statusDaLista.extend(statusDaLista)
impostors = [i for i, value in enumerate(statusDaLista) if value =='IMPOSTOR']
for k in range(len(impostors)):
    for i in range(len(statusDaLista)):
        if statusDaLista[i] != "IMPOSTOR":
            DistanciasY.append(abs(i-impostors[k]))
        else:
            DistanciasY.append(0)

for k in range(jogadoresTOP):
    DistanciasX.append(DistanciasY[k])
    for j in range(len(impostors)+1):
        DistanciasX[k] = min(DistanciasY[k+j*jogadoresTOP],DistanciasX[k])

    eliminated = [i for i, value in enumerate(DistanciasX) if value == max(DistanciasX)]
for index in eliminated:
    print(nomesDaLisTA[index])
