from entidade.barco_super import *
from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.portaavioes import Portaavioes

class ControladorBarcoSuper():
    def __init__(self, controlador_sistema):
        self.__lista_barco_historia = []
        self.__controlador_sistema = controlador_sistema
    
    @property
    def lista_barco_historio(self):
        return self.__lista_barco_historia
        
    @lista_barco_historio.setter
    def lista_barco_historia(self, lista_barco_historia):
        self.__lista_barco_historia= lista_barco_historia

    
        
    
    def listar_barcos(self):
        aux_lista_barcos = []
        for i in range (2):
            aux_lista_barcos.append(Bote())
        for i in range (0):
            aux_lista_barcos.append(Submarino())
        for i in range (0):
            aux_lista_barcos.append(Fragata())
        for i in range (0):
            aux_lista_barcos.append(Portaavioes())

        self.__lista_barco_historia.append(aux_lista_barcos)
        return aux_lista_barcos
    
    def destruido(self, barcos):
        
        for barco in barcos:
            checades=0
            for posicao in barco.posicoes:
                if posicao[2] == False:
                    checades+=1
            if checades>= barco.tamanho:
                BarcoSuper.desbarco(self, barco)

    def tomoutiro(self, barcos, valory, valorx):
        contavivo=False
        for barco in barcos:
            for pos in barco.posicoes:
                if pos[0] == valory-1 and pos[1] == valorx-1:
                    if pos[2]==True:
                        pos[2]=False
                        contavivo = True
        
        if contavivo==False: 
            return False
        else:
             return True

##########################################################
    
    def adicionar_posicao(self, oceano, barcos):
        for barco in barcos:
            posicao = self.__controlador_sistema.tela_partida.adicionar_posicao(barco, oceano, barcos)
            barco.posiciona(posicao)
            
            if barco.tamanho>1:
                self.__controlador_sistema.tela_partida.continuar_posicao(barco, oceano, barcos, posicao)
                
    def adicionar_posicao_comp(self, oceano, barcos_comp):
        for barco in barcos_comp:
            posicao = self.__controlador_sistema.tela_partida.adicionar_posicao_comp(barco, oceano, barcos_comp)
            barco.posiciona(posicao)
            if barco.tamanho>1:
                self.__controlador_sistema.tela_partida.continuar_posicao_comp(barco, oceano, barcos_comp, posicao)
            

