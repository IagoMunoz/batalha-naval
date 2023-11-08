from abc import abstractmethod, ABC
from entidade.oceano import Oceano
from controle.controladorSistema import *

class BS(ABC):
    @abstractmethod
    def __init__(self, nome, tamanho):
        self.__posicoes = []
        self.__estado = True
        self.__nome = nome
        self.__tamanho = tamanho
         
    @property
    def posicoes(self):
        return self.__posicoes

        
    @posicoes.setter
    def posicoes(self, posicoes):
        self.__posicoes= posicoes
        
    @property
    def estado(self):
        return self.__estado
        
    @estado.setter
    def estado(self, estado):
        self.__estado= estado
        
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome= nome
        
    @property
    def tamanho(self) -> int:
        return self.__tamanho
        
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho= tamanho

    def posiciona(self, posicao):
        auxposbarco=[posicao[0], posicao[1], True]
        self.__posicoes.append(auxposbarco)

    def continuar_posicao(self, coordenada, posicao):

        for casas in range(self.tamanho-1):
            if coordenada=="esquerda":
                self.posiciona((posicao[0], posicao[1]-(casas+1)))
        
        
            if coordenada=="direita":
                self.posiciona((posicao[0], posicao[1]+(casas+1)))

        
            if coordenada=="cima":
                self.posiciona((posicao[0]-(casas+1), posicao[1]))
        
        
            if coordenada=="baixo":
                self.posiciona((posicao[0]+(casas+1), posicao[1]))

    def tomoutiro(self, y, x):
        for posicao in self.posicoes:
            if posicao[0]==y and posicao[1]==x:
                posicao[2]=False


    def desbarco(self, barco):
        barco.estado= False
        
    
