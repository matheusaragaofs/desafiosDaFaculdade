mov1 = str(input()).lower()
contMov = 0
if mov1 =='esquerda' or mov1 == 'direita' or mov1 =='cima' or mov1 =='baixo':
    mov2 = str(input()).lower()
    contMov+=1
    if mov1 == 'cima' and mov2 == 'baixo' or mov1 == 'baixo' and mov2 == 'cima' or mov1 == 'esquerda' and mov2 == 'direita' or mov1 == 'direita' and mov2 == 'esquerda':
        print(f'Aang realizou somente {contMov} movimento')
    elif mov2 != 'esquerda' and mov2 != 'direita' and mov2 != 'cima' and mov2 != 'baixo':
        print(f'Aang relizou {contMov} movimento e tentou algo estranho, deve estar com a cabeca em outro lugar')

    else:
        mov3 = str(input()).lower()
        contMov+=1
        if mov2 == 'cima' and mov3 == 'baixo' or mov2 =='baixo' and mov3=='cima' or  mov2 == 'esquerda' and mov3=='direita' or mov2=='direita' and mov3=='esquerda':
            print(f'Aang realizou somente {contMov} movimentos')
        elif mov3 != 'esquerda' and mov3 != 'direita' and mov3 != 'cima' and mov3 != 'baixo':
            print(f'Aang realizou {contMov} movimentos e tentou algo estranho, deve estar com a cabeca em outro lugar')

        else:
            mov4 = str(input()).lower()
            contMov+=1
            if mov3 == 'cima' and mov4 == 'baixo' or mov3 == 'baixo' and mov4 == 'cima' or mov3 == 'esquerda' and mov4 == 'direita' or mov3 == 'direita' and mov4 == 'esquerda':
                print(f'Aang realizou somente {contMov} movimentos')
            elif  mov4 != 'esquerda' and mov4 != 'direita' and mov4 != 'cima' and mov4 != 'baixo':
                print(f'Aang realizou {contMov} movimentos e tentou algo estranho, deve estar com a cabeca em outro lugar')
            else:
                mov5 = str(input()).lower()
                contMov+=1
                if mov4 == 'cima' and mov5 == 'baixo' or mov4 =='baixo' and mov5=='cima' or  mov4== 'esquerda' and mov5=='direita' or mov4=='direita' and mov5=='esquerda':
                    print(f'Aang realizou somente {contMov} movimentos')
                elif mov5 != 'esquerda' and mov5 != 'direita' and mov5 != 'cima' and mov5 != 'baixo':
                    print(f'Aang realizou {contMov} movimentos e tentou algo estranho, deve estar com a cabeca em outro lugar')
                else:
                    contMov+=1
                    print(f'Aang realizou todos os {contMov} movimentos e conseguiu dobrar agua')
else:
    print('Aang nao realizou nenhum movimento comum, deve estar com a cabeca em outro lugar')






