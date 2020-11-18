qtdPontosNecessarios = int(input())
tamListaPontuação = int(input())

pontosEliteLIST = []
pontosRaimonLIST = []
PontuacaoEscolaRaimon = list(map(int, input().split()))
PontuacaoEscolaElite = list(map(int, input().split()))
gols = input().split()

def VerificarPontuacao(Raimon,Elite,PontosNecessarios):
    if sum(PontuacaoEscolaRaimon) >= qtdPontosNecessarios or sum(PontuacaoEscolaElite) >= qtdPontosNecessarios:
        return print("Parece que as regras desse campeonato falharam")
    else:
        return ('É possível')



def Pontuacao():
    if sum(PontuacaoEscolaRaimon) >= qtdPontosNecessarios or sum(PontuacaoEscolaElite) >= qtdPontosNecessarios:
        exit()


    else:
        contRaimon = 0
        contElite = 0
        pontosElite = 0
        pontosRaimon = 0
        for indexGols, gol in enumerate(gols):
            if gol == 'R':

                pontosRaimonLIST.append(PontuacaoEscolaRaimon[contRaimon%tamListaPontuação])
                pontosRaimon += PontuacaoEscolaRaimon[contRaimon%tamListaPontuação]
                contRaimon += 1

            if gol == 'E':
                pontosElite += PontuacaoEscolaElite[contElite%tamListaPontuação]
                pontosEliteLIST.append(PontuacaoEscolaElite[contElite%tamListaPontuação])
                contElite+=1

            if pontosElite >= qtdPontosNecessarios or pontosRaimon >= qtdPontosNecessarios:
                break

        if pontosRaimon > pontosElite :
            print('A escola Raimon saiu vitoriosa')
            print(f'Raimon: {pontosRaimon} ({len(pontosRaimonLIST)})')
            print(f'Elite: {pontosElite} ({len(pontosEliteLIST)})')

        if pontosElite > pontosRaimon:
            print('A escola Elite saiu vitoriosa')
            print(f'Elite: {pontosElite} ({len(pontosEliteLIST)})')
            print(f'Raimon: {pontosRaimon} ({len(pontosRaimonLIST)})')

VerificarPontuacao(pontosRaimonLIST,pontosEliteLIST,qtdPontosNecessarios)
Pontuacao()



