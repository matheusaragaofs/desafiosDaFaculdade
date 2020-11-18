valores = input().split()
instantes = []
instantes_soma = []
soma = []
contador = -1
existe = False
for valor in valores:
        if valor == "staring" and existe == False:
            contador += 1
            instantes.append(contador)
        else:
            if valor == "away":
                existe = True
                contador += 1
                instantes_soma.append(contador)
                soma.append(valor)
            else:
                if valor == 'staring' and existe == True:
                    contador += 1
                    instantes_soma.append(contador)
                    soma.append(valor)
if instantes == []:
    valor_final = sum(instantes_soma) % 2
else:
    valor_final = (sum(instantes_soma) + instantes.pop()) % 2

if valor_final == 0:
    print('Só mais um surto do Yusuke...')
else:
    if valor_final == 1:
        print('Salve-se quem puder!')