eventos =  int(input())
pessoas_infectadadas_inicialmente = int(input())
valor_Atual = pessoas_infectadadas_inicialmente
resultados = [ ]
for i in range(0,eventos):
    descricoes = str(input())
    if descricoes == 'INFECTADOS':
        num_Infectados = int(input())
        valor_Atual +=num_Infectados
        resultados.append(valor_Atual)
    elif descricoes == 'ESTUDOS APONTAM':
        num_estudos_apontam = int(input())
        if num_estudos_apontam > valor_Atual:
            resultados.append('FAKE NEWS')
            resultados.append(valor_Atual)
        elif num_estudos_apontam < valor_Atual:
            resultados.append('DESTA VEZ ELES ESTAO CERTOS')
            valor_Atual = num_estudos_apontam
            resultados.append(valor_Atual)
    elif descricoes == 'CLOROFILA NELES':
            valor_Atual = valor_Atual // 2
            if valor_Atual <1:
                resultados.append("O REI NOS SALVOU")
                break
            else:
                clorofila = valor_Atual
                resultados.append(clorofila)

for x in resultados:
    print(x)