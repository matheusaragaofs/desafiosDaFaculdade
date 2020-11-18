def calcular(lista_de_controle_de_pontos, t):
  lista_de_controle_de_pontos_len = len(lista_de_controle_de_pontos)
  tupla_de_pontos = []

  for i in range(lista_de_controle_de_pontos_len-1):
    if i < lista_de_controle_de_pontos_len-1:
      ponto_A, ponto_B = lista_de_controle_de_pontos[i]
      ponto_A = ponto_A* (1-t)
      ponto_B = ponto_B * (1-t)

      ponto_C, ponto_D = lista_de_controle_de_pontos[i+1]
      ponto_C = ponto_C * t
      ponto_D = ponto_D * t

    resultado = ponto_A + ponto_C, ponto_B + ponto_D
    tupla_de_pontos.append(resultado)

  if len(tupla_de_pontos) == 1: return tupla_de_pontos[0]
  else: return calcular(tupla_de_pontos, t)
  
  return tupla_de_pontos

lista_de_controle_de_pontos = []

controle_de_point_num = int(input())

for i in range(controle_de_point_num):  
  controle_de_ponto_A, controle_de_ponto_B = list(map(int, input().split()))
  lista_de_controle_de_pontos.append((controle_de_ponto_A, controle_de_ponto_B))

quantidade_de_T = int(input())

for i in range(quantidade_de_T):
  t = float(input())  
  ponto_X, ponto_Y = calcular(lista_de_controle_de_pontos, t)

  print(f"{ponto_X:.2f} {ponto_Y:.2f}") 