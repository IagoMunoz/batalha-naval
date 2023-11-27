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
        self.__lista_barco_historia = lista_barco_historia

    def listar_barcos(self):
        aux_lista_barcos = []
        for i in range (4):
            aux_lista_barcos.append(Bote())
        for i in range (3):
            aux_lista_barcos.append(Submarino())
        for i in range (3):
            aux_lista_barcos.append(Fragata())
        for i in range (1):
            aux_lista_barcos.append(Portaavioes())

        self.__lista_barco_historia.append(aux_lista_barcos)
        return aux_lista_barcos

    def destruido(self, barcos):

        for barco in barcos:
            checades = 0
            for posicao in barco.posicoes:
                if posicao[2] == False:
                    checades += 1
            if checades >= barco.tamanho:
                if barco.estado == True:
                    self.desbarco(barco)
          

    def desbarco(self, barco):
        barco.estado= False

    def tomoutiro(self, barcos, valory, valorx):
        self.__controlador_sistema.controlador_rodada.aux_acertos = 0
        contavivo = False
        for barco in barcos:
            for pos in barco.posicoes:
                if pos[0] == valory-1 and pos[1] == valorx-1:
                    if pos[2] == True:
                        pos[2] = False
                        contavivo = True
                        self.destruido(barcos)
                        if barco.estado==False:
                            self.__controlador_sistema.controlador_rodada.aux_acertos = 3

        if contavivo==False: 
            return False
        else:
             return True

##########################################################

    def adicionar_posicao(self, oceano, barcos):
        dic_barcos = []
        for dic_obj in barcos:
            dic_barcos.append(vars(dic_obj))
        
        relogio = len(barcos)
        for ponteiro in range(relogio):
            meajuda= True
            while meajuda == True:

                posicao = self.__controlador_sistema.tela_partida.adicionar_posicao(dic_barcos[ponteiro], oceano, dic_barcos)
                barcos[ponteiro].posiciona(posicao)
                

                if barcos[ponteiro].tamanho > 1:
                    continuar_pos = self.__controlador_sistema.tela_partida.continuar_posicao(dic_barcos[ponteiro], oceano, dic_barcos, posicao)
                    meajuda=continuar_pos
                    if meajuda ==True:
                        self.__controlador_sistema.tela_partida.repos()
                        barcos[ponteiro].desposiciona()
                    else:


                        continuar_pos = continuar_pos.title()
                        barcos[ponteiro].continuar_posicao(continuar_pos, posicao)
                else:
                    meajuda = posicao

    def adicionar_posicao_comp(self, oceano, barcos):
        dic_barcos = []
        for dic_obj in barcos:
            dic_barcos.append(vars(dic_obj))

        relogio = len(barcos)
        for ponteiro in range(relogio):
            meajuda= True
            while meajuda == True:

                posicao = self.__controlador_sistema.tela_partida.adicionar_posicao_comp(dic_barcos[ponteiro], oceano, dic_barcos)
                barcos[ponteiro].posiciona(posicao)

                if barcos[ponteiro].tamanho > 1:
                    continuar_pos = self.__controlador_sistema.tela_partida.continuar_posicao_comp(dic_barcos[ponteiro], oceano, dic_barcos, posicao)
                    meajuda=continuar_pos
                    if meajuda !=True:

                        continuar_pos = continuar_pos.title()
                        barcos[ponteiro].continuar_posicao(continuar_pos, posicao)

                    
                else:
                    meajuda = posicao
