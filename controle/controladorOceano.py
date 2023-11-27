from entidade.oceano import Oceano
from controle.controlador_barco_super import *
import random


class ControladorOceano():
    def __init__(self, controlador_sistema):
        self.__oceanos = []
        self.__controlador_sistema = controlador_sistema

    @property
    def oceanos(self):
        return self.__oceanos

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @oceanos.setter
    def oceanos(self, oceanos):
        self.__oceanos=oceanos

    def cria_oceano(self):
        tamanhos = self.__controlador_sistema.tela_partida.seleciona_jogo()
        while True:
            if tamanhos == None:
                tamanhos = self.__controlador_sistema.tela_partida.seleciona_jogo()
            else:
                break
        oceanoaux = Oceano(random.randint(1, 1000000000000), tamanhos, self.cria_matriz_oceano(tamanhos))
        self.__oceanos.append(oceanoaux)
        return oceanoaux

    def cria_matriz_oceano(self, tamanhos):
        aux_matriz_oceano = []
        for y in range (tamanhos[0]):
            aux_matriz = []
            for x in range (tamanhos[1]):
                aux_matriz.append(x)
            aux_matriz_oceano.append(aux_matriz)
        return(aux_matriz_oceano)

    def cria_oceano_comp(self):
        ultimooceano=len(self.oceanos)-1
        tamanhos = self.oceanos[ultimooceano].tamanhos
        oceanoaux = Oceano((random.randint(1, 1000000000000)), tamanhos, self.cria_matriz_oceano(tamanhos))
        self.__oceanos.append(oceanoaux)
        return oceanoaux