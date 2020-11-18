pilotosY = {}
ResultadosZ = {}

numero_de_premios, numero_de_pilotosY = list(map(int, input().split()))

for i in range(numero_de_pilotosY):
  pilotosY[i+1] = []

for i in range(numero_de_premios):
  ordem_de_chegadaW = list(map(int, input().split()))
  for j in range(len(ordem_de_chegadaW)):
    pilotosY[j+1].append(ordem_de_chegadaW[j])

pontuação = int(input())

for i in range(pontuação):
  pontuação = {}
  resultado_do_piloto = {}
  pontuacao_K = list(map(int, input().split()))

  for j in range(len(pontuacao_K)):
    pontos = pontuacao_K[j]
    pontuação[j+1] = pontos

  for pilot in pilotosY:
    ResultadosZ[pilot] = 0

  for key, value in pilotosY.items():
    for i in range(numero_de_premios):
      if not value[i] > len(pontuação.keys()):
        ResultadosZ[key] += pontuação[value[i]]
    
  lugar = [ k for k, v in ResultadosZ.items() if v == max(ResultadosZ.values()) ]  
  print(str(lugar).strip('[]').replace(',', ''))