oceano = [[1,2,3],[1,2,3],[1,2,3]]
jatiro = []

from entidade.bote import Bote

a = bote()








for ycolunas in range(len(oceano)):
    for xlinha in range(len(oceano[ycolunas])):
        tembarco=False
        for barco in barcos:
            for posicao in barco['_BS__posicoes']:
                if posicao[0]==ycolunas and posicao[1]==xlinha:
                    if barco['_BS__estado']==True:
                        if posicao[2]==True:
                            if len(barco['_BS__posicoes'])==1:
                                oceano[ycolunas][xlinha] = barco['_BS__nome']
                                tembarco = True
                            else:
                                oceano[ycolunas][xlinha] = 'barco'
                                tembarco=True
                        else:
                            oceano[ycolunas][xlinha] = 'barco'
                            tembarco=True
                    else:
                        oceano[ycolunas][xlinha] = barco['_BS__nome']
                        tembarco=True

        if tembarco == False:
            marzin=True
            for jatiroin in jatiro:
                if jatiroin[0] == ycolunas+1 and jatiroin[1] == xlinha+1:
                    oceano[ycolunas][xlinha] = 'mar'
                    marzin=False
            if marzin==True:
                oceano[ycolunas][xlinha] = 'mar'