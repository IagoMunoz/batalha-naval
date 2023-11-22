from controle.controladorPartida import ControladorPartida
from controle.controlador_barco_super import ControladorBarcoSuper
import random

class TelaRodada():
    def __init__(self):
        self.__controlador_partida = ControladorPartida(self)

    @property
    def controlador_partida(self):
        return self.__controlador_partida
    
    def mostra_rodada(self, dados_rodada):
                print("RODADA")
                print("JOGADA DO JOGADOR: ", dados_rodada["coordenadas do jogador"])
                print("JOGADA DO COMPUTADOR: ", dados_rodada["coordenadas do computador"])
                print("PONTOS DO JOGADOR: ", dados_rodada["pontos do jogador"])
                print("PONTOS DO COMPUTADOR: ", dados_rodada["pontos do computador"])
                print("\n")
    
    
            
            #############################################################################
                
    def rodada1(self, oceano, barcos, jatiro):
        contx=1
        for y in range(len(oceano[0])):
            if y>8:
                print("",y+1,end='')
            else:
                print("",y+1,end=' ')
        print("")

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                    for posicao in barco['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:
                            if barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    print ('[~]', end='')
                                    tembarco=True
                                else:
                                    print('[%]',end='')
                                    tembarco=True
                            else:
                                print('[{}]'.format(barco['_BS__nome'][0]).lower(),end='')
                                tembarco=True

                if tembarco == False:
                    marzin=True
                    for jatiroin in jatiro:
                        if jatiroin[0] == ycolunas+1 and jatiroin[1] == xlinha+1:
                            print('[@]',end='')
                            marzin=False
                    if marzin==True:
                        print('[~]',end='')

            if contx==ycolunas:
                print(" ", contx)
            else:
                print("")
            contx+=1
        


    def escolhexy_rodada(self, oceano, barcos, jatiro):
        while True:
            try:
                valory ,valorx = map(int, input("Digite onde quer atirar linha e coluna: ").split())
                while True:
                    for tiro in jatiro:
                        if tiro[0]==valory and tiro[1]==valorx:
                            valory ,valorx = map(int, input("Valor já atirado. Digite onde quer atirar linha e coluna: ").split())
                        if valory>(len(oceano)) or valorx>(len(oceano[0])) or valorx<=0 or valory<=0:
                            valory,valorx = map(int, input("Valores errados. Digite novamente onde quer atirar linha e coluna: ").split())
                    else:
                        break
                        
                
            except ValueError:
                print('Valores inválidos')
            else:
                break
        

        contx=1
        for y in range(len(oceano[0])):
            if y+1==valorx:
                print("   ",valorx,end='')
            else:
                print(" ",end=' ')
        print("")

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                
                    
                    for posicao in ['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:

                            if valory-1==ycolunas and valorx-1==xlinha:
                                tembarco=True
                                print ('[X]',end='')
                                tembarco=True

                            elif barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    tembarco=True
                                    print ('[~]', end='')
                                    tembarco=True
                                else:
                                    tembarco=True
                                    print('[%]',end='')
                                    tembarco=True
                            else:
                                tembarco=True
                                print('[{}]'.format(barco['_BS__nome'][0]).lower(),end='')
                                tembarco=True
                        

                if tembarco == False:
                    marzin=True
                    for jatiroin in jatiro:
                        if jatiroin[0] == ycolunas+1 and jatiroin[1] == xlinha+1:
                            print('[@]',end='')
                            marzin=False
                    if marzin==True:
                        if valory-1==ycolunas and valorx-1==xlinha:
                            print ('[X]',end='')
                        else:
                            print('[~]',end='')
                        
                    

            if contx==valory:
                print("", contx)
            else:
                print("")
            contx+=1


        uauaux=input('deseja syirar ai msm esta posicao? [s/n]: ')
        if uauaux=="s":
            return (valory, valorx, True)
        
            
        
        #retorna true se acerta e false se erra
        
            
        ####################################################################################
    def conc_rodada(self, jogadnv, acertou):
        if jogadnv==True:
            
            acertou+=1
            
           
            print('Parabéns! Você acertou a jogada')
            
        else:
            print('Você errou a jogada! :(')

        return acertou
        
                    


        

                    

            
    def rodada1_comp(self, oceano, barcos, jatiro):
        contx=1
        for y in range(len(oceano[0])):
            if y>8:
                print("",y+1,end='')
            else:
                print("",y+1,end=' ')
        print("")

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                    for posicao in barco['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:
                            if barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    print ('[~]', end='')
                                    tembarco=True
                                else:
                                    print('[%]',end='')
                                    tembarco=True
                            else:
                                print('[{}]'.format(barco['_BS__nome'][0]).lower(),end='')
                                tembarco=True

                if tembarco == False:
                    marzin=True
                    for jatiro in jatiro:
                        if jatiro[0] == ycolunas+1 and jatiro[1] == xlinha+1:
                            print('[@]',end='')
                            marzin=False
                    if marzin==True:
                        print('[~]',end='')

            if contx==ycolunas:
                print(" ", contx)
            else:
                print("")
            contx+=1


    def escolhexy_rodada_comp(self, oceano, barcos, jatiro):
                
        print("computador irá atirar")
        print("")
        while True:
            aux = 0
            valory = (random.randint(1, (len(oceano))))
            valorx = (random.randint(1, (len(oceano[0]))))
            for tiro in jatiro:
                if tiro[0]==valory or tiro[1]==valorx:
                    valory = (random.randint(1, (len(oceano))))
                    valorx = (random.randint(1, (len(oceano[0]))))
                else:
                    aux +=1
            if aux==len(jatiro):
                break
                            
                    

        contx=1
        for y in range(len(oceano[0])):
            if y+1==valorx:
                print("   ",valorx,end='')
            else:
                print(" ",end=' ')
        print("")

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                
                    
                    for posicao in ['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:

                            if valory-1==ycolunas and valorx-1==xlinha:
                                tembarco=True
                                print ('[X]',end='')
                                tembarco=True

                            elif barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    tembarco=True
                                    print ('[~]', end='')
                                    tembarco=True
                                else:
                                    tembarco=True
                                    print('[%]',end='')
                                    tembarco=True
                            else:
                                tembarco=True
                                print('[{}]'.format(barco['_BS__nome'][0]).lower(),end='')
                                tembarco=True
                        

                if tembarco == False:
                    marzin=True
                    for jatiro in jatiro:
                        if jatiro[0] == ycolunas+1 and jatiro[1] == xlinha+1:
                            print('[@]',end='')
                            marzin=False
                    if marzin==True:
                        if valory-1==ycolunas and valorx-1==xlinha:
                            print ('[X]',end='')
                        else:
                            print('[~]',end='')
                        
                    

            if contx==valory:
                print("", contx)
            else:
                print("")
            contx+=1

        return (valory, valorx, True)
                
    def conc_rodada_comp(self, jogadnv, acertou):
        if jogadnv==True:
            
            acertou+=1
            
           
            print('IH ALA O COMPIUTER ACERTOU')
            
        else:
            print('computador errou! :)')

        return acertou
        