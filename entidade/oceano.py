from controle.controladorSistema import *


class Oceano():
    def __init__(self, id, tamanhos, oceano):
        #botar excecao para caso seja maior que a tela do jogo (600x800)
        self.__id = id
        self.__tamanhos = tamanhos
        self.__oceano = oceano

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id= id

    @property
    def tamanhos(self):
        return self.__tamanhos

    @tamanhos.setter
    def tamanhos(self, tamanhos):
        self.__tamanhos= tamanhos

    @property
    def barcos(self):
        return self.__barcos

    @barcos.setter
    def barcos(self, barcos):
        self.__barcos= barcos

    @property
    def oceano(self):
        return self.__oceano

    @oceano.setter
    def oceano(self, oceano):
        self.__oceano= oceano