pessoas = {}
campos_que_faltam = {}
camposX = []

while True:
  try:
    nome, campo = input().split()

    if campo not in camposX:
      camposX.append(campo)
    if nome not in pessoas:
      pessoas[nome] = []
    
    pessoas[nome].append(campo)
    
  except EOFError:
    for pessoaY in pessoas:
      campos_que_faltam[pessoaY] = []
      for campo in camposX:
        if campo not in pessoas[pessoaY]:
          campos_que_faltam[pessoaY].append(campo)

    for pessoaY in campos_que_faltam:
      print(f"{pessoaY}:")
      for item in campos_que_faltam[pessoaY]:
        print(f"- {item}")
    break