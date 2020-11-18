lancesPartida = int(input())
Acoes = ['GOL','ASSISTENCIA','AMARELO','VERMELHO','IMPEDIMENTO']
Pontos =[3.5,2,-1.5,-4,-1]
TodasNotas= [ ]
pontosPancorbo= pontosFernandez= pontosMomprevil= pontosEchevarria= pontosTaladro =0

for i in range (0,lancesPartida):
    Lances = str(input()).split()
    if Lances[1] == 'Pancorbo':
        for x in Acoes:
            if x == Lances[0]:
               indexAcoes = Acoes.index(x)
               pontosPancorbo += Pontos[indexAcoes]
    elif Lances[1] == 'Fernandez':
        for x in Acoes:
            if x == Lances[0]:
               indexAcoes = Acoes.index(x)
               pontosFernandez += Pontos[indexAcoes]
    elif Lances[1] == 'Momprevil':
        for x in Acoes:
            if x == Lances[0]:
                indexAcoes = Acoes.index(x)
                pontosMomprevil += Pontos[indexAcoes]
    elif Lances[1] == 'Echevarria':
        for x in Acoes:
            if x == Lances[0]:
               indexAcoes = Acoes.index(x)
               pontosEchevarria += Pontos[indexAcoes]
    elif Lances[1] == 'Taladro':
        for x in Acoes:
            if x == Lances[0]:
               indexAcoes = Acoes.index(x)
               pontosTaladro += Pontos[indexAcoes]
notasNormalizadas = [ ]
TodasNotas.append(pontosPancorbo)
TodasNotas.append(pontosFernandez)
TodasNotas.append(pontosMomprevil)
TodasNotas.append(pontosEchevarria)
TodasNotas.append(pontosTaladro)
maxNota = max(TodasNotas)
minNota = min(TodasNotas)
# print(TodasNotas)
# print(maxNota)
# print(minNota)
# if pontosEchevarria == pontosTaladro == pontosFernandez == pontosPancorbo == pontosMomprevil:
if maxNota == minNota:
    notasNormalizadas = [5,5,5,5,5]

else:
    normalPancorbo = ((pontosPancorbo - minNota) / (maxNota - minNota))*10
    normalFernandez = ((pontosFernandez-minNota) / (maxNota-minNota))*10
    normalMomprevil = ((pontosMomprevil-minNota) / (maxNota - minNota))*10
    normalEchevarria = ((pontosEchevarria-minNota) / (maxNota-minNota))*10
    normalTaladro = ((pontosTaladro-minNota) / (maxNota-minNota))*10
    notasNormalizadas.append(normalPancorbo)
    notasNormalizadas.append(normalFernandez)
    notasNormalizadas.append(normalMomprevil)
    notasNormalizadas.append(normalEchevarria)
    notasNormalizadas.append(normalTaladro)
# print(notasNormalizadas)


Pessoas = ['Pancorbo','Fernandez','Momprevil','Echevarria','Taladro']

for z in range(len(Pessoas)):
    if notasNormalizadas[z]>=7.5:
        print(f'O {Pessoas[z]} tirou uma nota de {notasNormalizadas[z]:.2f} pontos! Que atuacao espetacular!')
    elif 5<=notasNormalizadas[z]<=7.5:
        print(f'O {Pessoas[z]} ficou com uma nota de {notasNormalizadas[z]:.2f} pontos!')
    elif 2.5<= notasNormalizadas[z] <=5:
        print(f'O {Pessoas[z]} decepcionou o publico presente no estadio com uma nota de {notasNormalizadas[z]:.2f} pontos!')
    elif notasNormalizadas[z] >=0:
        print(f'O {Pessoas[z]} foi o bola murcha da partida com apenas {notasNormalizadas[z]:.2f} pontos! Ele sai vaiado do estadio.')