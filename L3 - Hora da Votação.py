num_votes = int(input())
impostor = input()
names = []
votes = []
counting = []
draw = False
higher = 0
for person in range(num_votes):
    votante,voto = input().split()
    votante = votante.replace(':','')
    if votante not in names:
        names.append(votante)
    if voto not in names:
        names.append(voto)
    votes.append(voto)
for voter in names:
    contador = votes.count(voter)
    counting.append(int(contador))

for i in counting:
    if i > higher:
        higher=i
        draw=False
    elif i == higher:
        draw =True
if len(names) > num_votes:
    print(f'Votação incompleta. Faltam votos de {len(names)-num_votes} jogadores')
    draw = False
    if draw == True:
        print('Empate. Ninguem foi expulso')
elif len(names) == num_votes:
    if draw ==True:
        print('Empate. Ninguem foi expulso')
    else:
        eliminated = names[counting.index(higher)]
        if eliminated == impostor:
            print(f'{eliminated} foi expulso com {higher} votos. Ele era o IMPOSTOR')
        else:
            if eliminated != impostor:
                print(f'{eliminated} foi expulso com {higher} votos. Ele era INOCENTE')