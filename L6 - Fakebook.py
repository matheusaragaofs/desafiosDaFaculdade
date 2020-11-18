def amigo(pessoa, pessoas, amizades):
  if pessoa not in amizades:
    amizades.append(pessoa)
    for pessoaY in pessoas[pessoa]:
      amigo(pessoaY, pessoas, amizades)
  return amizades

pessoas = {}
amizades = []
citações_pessoas = int(input())

for i in range(citações_pessoas):
  pessoas[input()] = []

amizade_no_direct_numeros = int(input())

for i in range(amizade_no_direct_numeros):
  pessoa1, pessoa2 = input().split()
  pessoas[pessoa1].append(pessoa2)
  pessoas[pessoa2].append(pessoa1)

numero_caso_de_testes = int(input())

for i in range(numero_caso_de_testes):
  pessoa1, pessoa2 = input().split()

  if pessoa1 in pessoas[pessoa2]: 
    print('SIM')
    break

  else:
    resultado = amigo(pessoa1, pessoas, amizades)

    if pessoa2 in resultado: print('SIM')
    else: print('NAO')