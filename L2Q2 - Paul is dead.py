qtd_albuns = int(input())
discosVendidosX = musicasPorAlbumX =0
for i in range(qtd_albuns):
    if i%2==0:
        #RAVI
        discosVendidos = input()
        musicasPorAlbum = input()
        if discosVendidos.isnumeric() == False or musicasPorAlbum.isnumeric() == False:
            discosVendidosX+=0
            musicasPorAlbumX+=0
            qtd_albuns-=1
        else:
            discosVendidos = int(discosVendidos)
            discosVendidosX+=discosVendidos
            musicasPorAlbum = int(musicasPorAlbum)
            musicasPorAlbumX += musicasPorAlbum

    if i%2!=0:
        #RODRIGO
        musicasPorAlbum = input()
        discosVendidos = input()
        if discosVendidos.isnumeric() == False or musicasPorAlbum.isnumeric() == False:
            discosVendidosX += 0
            musicasPorAlbumX += 0
            qtd_albuns-=1
        else:
            musicasPorAlbum= int(musicasPorAlbum)
            musicasPorAlbumX+= musicasPorAlbum
            discosVendidos = int(discosVendidos)
            discosVendidosX += discosVendidos



if qtd_albuns == 0:
    mediaDiscos = 0
    mediaMusicas= 0
else:
    mediaDiscos = discosVendidosX/qtd_albuns
    if mediaDiscos == 0:
        mediaMusicas =0
    else:
        mediaMusicas = musicasPorAlbumX/qtd_albuns
print(f'{mediaDiscos:.2f}')
print(f'{mediaMusicas:.2f}')
