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
    
    def atira(self, oceano, barcos, jogadnv, acertou, tiros):
        while jogadnv==True:
            ControladorBarcoSuper.destruido(self, barcos)   

            poretorna=False
            valory=0
            valorx=0
            while poretorna==False:
                
                 
                contx=1
                for y in range(len(oceano.oceano[0])):
                    if y>8:
                        print("",y+1,end='')
                    else:
                        print("",y+1,end=' ')
                print("")

                for ycolunas in range(len(oceano.oceano)):
                    for xlinha in range(len(oceano.oceano[y])):
                        tembarco=False
                        for barco in barcos:
                            for posicao in barco.posicoes:
                                if posicao[0]==ycolunas and posicao[1]==xlinha:
                                    if barco.estado==True:
                                        if posicao[2]==True:
                                            print ('[~]', end='')
                                            tembarco=True
                                        else:
                                            print('[%]',end='')
                                            tembarco=True
                                    else:
                                        print('[{}]'.format(barco.nome[0]).lower(),end='')
                                        tembarco=True

                        if tembarco == False:
                            marzin=True
                            for jatiro in self.__controlador_partida.jatiro:
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
                


                print(self.__controlador_partida.jatiro)
                while True:
                    try:
                        valory ,valorx = map(int, input("Digite onde quer atirar linha e coluna: ").split())
                        while True:
                            for tiro in self.__controlador_partida.jatiro:
                                if tiro[0]==valory and tiro[1]==valorx:
                                    valory ,valorx = map(int, input("Valor já atirado. Digite onde quer atirar linha e coluna: ").split())
                                if valory>(oceano.tamanhos[0]) or valorx>(oceano.tamanhos[1]) or valorx<=0 or valory<=0:
                                    valory,valorx = map(int, input("Valores errados. Digite novamente onde quer atirar linha e coluna: ").split())
                            else:
                                break
                                
                        
                    except ValueError:
                        print('Valores inválidos')
                    else:
                        break
                

                contx=1
                for y in range(len(oceano.oceano[0])):
                    if y+1==valorx:
                        print("   ",valorx,end='')
                    else:
                        print(" ",end=' ')
                print("")

                for ycolunas in range(len(oceano.oceano)):
                    for xlinha in range(len(oceano.oceano[y])):
                        tembarco=False
                        for barco in barcos:
                        
                           
                            for posicao in barco.posicoes:
                                if posicao[0]==ycolunas and posicao[1]==xlinha:

                                    if valory-1==ycolunas and valorx-1==xlinha:
                                        tembarco=True
                                        print ('[X]',end='')
                                        tembarco=True

                                    elif barco.estado==True:
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
                                        print('[{}]'.format(barco.nome[0]).lower(),end='')
                                        tembarco=True
                                

                        if tembarco == False:
                            marzin=True
                            for jatiro in self.__controlador_partida.jatiro:
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


                uauaux=input('deseja syirar ai msm esta posicao? [s/n]: ')
                if uauaux=="s":
                    seracertou = ControladorBarcoSuper.tomoutiro(self, barcos, valory, valorx)
                    self.__controlador_partida.add_jatiro([valory,valorx])
                    jogadnv=seracertou

                    ControladorBarcoSuper.destruido(self,barcos)
                    poretorna=True
                
                #retorna true se acerta e false se erra
                print('')
            
            
            if jogadnv==True:
                
                acertou+=1
                
                tiros.append(valorx)
                tiros.append(valory)
                #fazer verificação dps pra qnd acertar a embarcação toda ir +3 pontos
                print('Parabéns! Você acertou a jogada')
                contvic=0
                for barco in barcos:
                    if barco.estado==True:

                        contvic+=1
                if contvic==0:
                    break
            else:
                print('Você errou a jogada! :(')
                tiros.append(valorx)
                tiros.append(valory)
        if acertou==0:
            return valorx, valory, acertou
        else:
            return tiros, acertou
        
                    


        

                    

            
    def atira_comp(self, oceano, barcos, jogadnv, acertou, tiros):
        print(jogadnv)
        print("tubarao")
        while jogadnv==True:
            print("tubarao")


            ControladorBarcoSuper.destruido(self, barcos)   

            poretorna=False
            valory=0
            valorx=0
            while poretorna==False:
                
                 
                contx=1
                for y in range(len(oceano.oceano[0])):
                    if y>8:
                        print("",y+1,end='')
                    else:
                        print("",y+1,end=' ')
                print("")

                for ycolunas in range(len(oceano.oceano)):
                    for xlinha in range(len(oceano.oceano[y])):
                        tembarco=False
                        for barco in barcos:
                            for posicao in barco.posicoes:
                                if posicao[0]==ycolunas and posicao[1]==xlinha:
                                    if barco.estado==True:
                                        if posicao[2]==True:
                                            print ('[{}]'.format(barco.nome[0]), end='')
                                            tembarco=True
                                        else:
                                            print('[%]',end='')
                                            tembarco=True
                                    else:
                                        print('[{}]'.format(barco.nome[0]).lower(),end='')
                                        tembarco=True

                        if tembarco == False:
                            marzin=True
                            for jatiro in self.__controlador_partida.jatiro_comp:
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

                print("")
                print("computador irá atirar")
                print("")
                while True:
                    aux = 0
                    valory = (random.randint(1, (oceano.tamanhos[0])))
                    valorx = (random.randint(1, (oceano.tamanhos[1])))
                    for tiro in self.__controlador_partida.jatiro_comp:
                        if tiro[0]==valory or tiro[1]==valorx:
                            valory = (random.randint(1, (oceano.tamanhos[0])))
                            valorx = (random.randint(1, (oceano.tamanhos[1])))
                        else:
                            aux +=1
                    if aux==len(self.__controlador_partida.jatiro_comp):
                        break
                            
                    

                contx=1
                for y in range(len(oceano.oceano[0])):
                    if y+1==valorx:
                        print("   ",valorx,end='')
                    else:
                        print(" ",end=' ')
                print("")

                for ycolunas in range(len(oceano.oceano)):
                    for xlinha in range(len(oceano.oceano[y])):
                        tembarco=False
                        for barco in barcos:
                        
                           
                            for posicao in barco.posicoes:
                                if posicao[0]==ycolunas and posicao[1]==xlinha:

                                    if valory-1==ycolunas and valorx-1==xlinha:
                                        tembarco=True
                                        print ('[X]3',end='')
                                        tembarco=True

                                    elif barco.estado==True:
                                        if posicao[2]==True:
                                            tembarco=True
                                            print ('[{}]'.format(barco.nome[0]), end='')
                                            tembarco=True
                                        else:
                                            tembarco=True
                                            print('[%]',end='')
                                            tembarco=True
                                    else:
                                        tembarco=True
                                        print('[{}]'.format(barco.nome[0]).lower(),end='')
                                        tembarco=True
                                

                        if tembarco == False:
                            marzin=True
                            for jatiro in self.__controlador_partida.jatiro_comp:
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


                
                poretorna=True
                
                #retorna true se acerta e false se erra
                print(oceano.tamanhos)
                seracertou = ControladorBarcoSuper.tomoutiro(self, barcos, valory, valorx)
                self.__controlador_partida.add_jatiro_comp([valory,valorx])
                jogadnv=seracertou

                ControladorBarcoSuper.destruido(self,barcos)

            if jogadnv==True:
                tiros.append(valorx)
                tiros.append(valory)
                acertou += 1
                print('compiuter acertou a jogada')
                contvic=0
                for barco in barcos:
                    if barco.estado==True:

                        contvic+=1
                if contvic==0:
                    break
            else:
                print('computers erroujogada! :(')
        if acertou==0:
            return [valorx, valory, acertou]
        else:
            return tiros, acertou
        